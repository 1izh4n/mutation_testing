from tcas.main import altitude_separation_test
from tcas.state import State


def make_state(**kwargs) -> State:
    defaults = dict(
        current_vertical_sep=0,
        high_confidence=1,
        two_of_three_reports_valid=1,
        own_tracked_altitude=0,
        own_tracked_alt_rate=100,
        other_tracked_altitude=0,
        altitude_layer_value=0,
        up_separation=0,
        down_separation=0,
        other_rac=0,
        other_capability=1,
        climb_inhibit=0,
    )
    defaults.update(kwargs)
    return State(**defaults)


def compute_top_from_trace(t):
    return (
        t["high_confidence"] and t["rate_ok"] and t["vert_sep_ok"]
    ) and ((t["other_cap_1"] and (t["two_reports"] and t["other_rac_0"])) or (not t["other_cap_1"]))


def test_active_clause_high_confidence():
    # toggle high_confidence while keeping others fixed -> changes top-level decision
    base = make_state(current_vertical_sep=700)
    t1 = {}
    altitude_separation_test(base, trace=t1)
    v1 = compute_top_from_trace(t1)

    mod = make_state(current_vertical_sep=700, high_confidence=0)
    t2 = {}
    altitude_separation_test(mod, trace=t2)
    v2 = compute_top_from_trace(t2)

    assert v1 != v2


def test_active_clause_rate_ok():
    # toggle own_tracked_alt_rate boundary
    base = make_state(current_vertical_sep=700, own_tracked_alt_rate=600)
    t1 = {}
    altitude_separation_test(base, trace=t1)
    v1 = compute_top_from_trace(t1)

    mod = make_state(current_vertical_sep=700, own_tracked_alt_rate=601)
    t2 = {}
    altitude_separation_test(mod, trace=t2)
    v2 = compute_top_from_trace(t2)

    assert v1 != v2


def test_active_clause_vert_sep():
    # toggle current_vertical_sep crossing >600
    base = make_state(current_vertical_sep=601)
    t1 = {}
    altitude_separation_test(base, trace=t1)
    v1 = compute_top_from_trace(t1)

    mod = make_state(current_vertical_sep=600)
    t2 = {}
    altitude_separation_test(mod, trace=t2)
    v2 = compute_top_from_trace(t2)

    assert v1 != v2


def test_active_clause_other_capability():
    # create circumstance where toggling other_capability changes top-level decision
    # set two_reports and other_rac such that when other_capability==1 the (D and (E and F)) is False
    base = make_state(current_vertical_sep=700, two_of_three_reports_valid=0, other_rac=1, other_capability=1)
    t1 = {}
    altitude_separation_test(base, trace=t1)
    v1 = compute_top_from_trace(t1)

    mod = make_state(current_vertical_sep=700, two_of_three_reports_valid=0, other_rac=1, other_capability=0)
    t2 = {}
    altitude_separation_test(mod, trace=t2)
    v2 = compute_top_from_trace(t2)

    assert v1 != v2


def test_active_clause_two_reports_or_rac():
    # toggle two_of_three_reports_valid and other_rac to show effect
    base = make_state(current_vertical_sep=700, two_of_three_reports_valid=1, other_rac=0)
    t1 = {}
    altitude_separation_test(base, trace=t1)
    v1 = compute_top_from_trace(t1)

    mod = make_state(current_vertical_sep=700, two_of_three_reports_valid=0, other_rac=1)
    t2 = {}
    altitude_separation_test(mod, trace=t2)
    v2 = compute_top_from_trace(t2)

    assert v1 != v2
