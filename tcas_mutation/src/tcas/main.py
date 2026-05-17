from .state import State


# --- threat checks ---
def own_below_threat(state: State) -> bool:
    return state.own_tracked_altitude < state.other_tracked_altitude


def own_above_threat(state: State) -> bool:
    return state.other_tracked_altitude < state.own_tracked_altitude


# --- RA threshold logic ---
def positive_ra_alt_thresh(state: State, layer: int) -> int:
    if layer == 0:
        return state.positive_ra_alt_thresh_0
    elif layer == 1:
        return state.positive_ra_alt_thresh_1
    elif layer == 2:
        return state.positive_ra_alt_thresh_2
    elif layer == 3:
        return state.positive_ra_alt_thresh_3
    return 0


def alim(state: State) -> int:
    return positive_ra_alt_thresh(state, state.altitude_layer_value)


def inhibit_biased_climb(state: State) -> int:
    return state.up_separation + 100 if state.climb_inhibit else state.up_separation


def non_crossing_biased_climb(state: State) -> bool:
    if inhibit_biased_climb(state) > state.down_separation:
        return (not own_below_threat(state)) or (
            own_below_threat(state) and not (state.down_separation >= alim(state))
        )
    else:
        return (
            own_above_threat(state)
            and (state.current_vertical_sep >= 300)
            and (state.up_separation >= alim(state))
        )


def non_crossing_biased_descend(state: State) -> bool:
    if inhibit_biased_climb(state) > state.down_separation:
        return (
            own_below_threat(state)
            and (state.current_vertical_sep >= 300)
            and (state.down_separation >= alim(state))
        )
    else:
        return (not own_above_threat(state)) or (
            own_above_threat(state) and (state.up_separation >= alim(state))
        )


def altitude_separation_test(state: State, trace: dict = None) -> int:
    alt_sep = 0

    # evaluate atomic clauses for tracing / MCDC-style checks
    c_high_confidence = bool(state.high_confidence)
    c_rate_ok = state.own_tracked_alt_rate <= 600
    c_vert_sep_ok = state.current_vertical_sep > 600
    c_other_cap_1 = state.other_capability == 1
    c_two_reports = bool(state.two_of_three_reports_valid)
    c_other_rac_0 = state.other_rac == 0

    if trace is not None:
        trace.update(
            {
                "high_confidence": c_high_confidence,
                "rate_ok": c_rate_ok,
                "vert_sep_ok": c_vert_sep_ok,
                "other_cap_1": c_other_cap_1,
                "two_reports": c_two_reports,
                "other_rac_0": c_other_rac_0,
            }
        )

    top_level_condition = (
        c_high_confidence and c_rate_ok and c_vert_sep_ok
    ) and ((c_other_cap_1 and (c_two_reports and c_other_rac_0)) or not c_other_cap_1)

    if top_level_condition:
        need_upward_RA = non_crossing_biased_climb(state) and own_below_threat(state)
        need_downward_RA = non_crossing_biased_descend(state) and own_above_threat(
            state
        )

        if trace is not None:
            trace.update(
                {
                    "need_upward_RA": bool(need_upward_RA),
                    "need_downward_RA": bool(need_downward_RA),
                }
            )

        if need_upward_RA and need_downward_RA:
            alt_sep = 0  # No advisory
        elif need_upward_RA:
            alt_sep = 1  # Upward RA
        elif need_downward_RA:
            alt_sep = 2  # Downward RA
        else:
            alt_sep = 0

    return alt_sep
