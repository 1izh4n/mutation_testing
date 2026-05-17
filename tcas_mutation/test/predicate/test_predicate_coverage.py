from tcas.main import altitude_separation_test
from tcas.state import State


def make_state(**kwargs) -> State:
    defaults = dict(
        current_vertical_sep=0,
        high_confidence=0,
        two_of_three_reports_valid=0,
        own_tracked_altitude=0,
        own_tracked_alt_rate=0,
        other_tracked_altitude=0,
        altitude_layer_value=0,
        up_separation=0,
        down_separation=0,
        other_rac=0,
        other_capability=0,
        climb_inhibit=0,
    )
    defaults.update(kwargs)
    return State(**defaults)


def test_top_level_condition_false():
    # satisfies: top-level predicate falsified (branch not taken)
    s = make_state(high_confidence=0, own_tracked_alt_rate=100, current_vertical_sep=700)
    assert altitude_separation_test(s) == 0


def test_top_level_condition_true_no_RA():
    # top-level true but neither upward nor downward needed -> returns 0
    s = make_state(
        high_confidence=1,
        own_tracked_alt_rate=100,
        current_vertical_sep=700,
        other_capability=0,  # makes second part True via `not (other_capability == 1)`
    )
    assert altitude_separation_test(s) == 0


def test_need_upward_RA():
    # construct a state where upward RA is required
    s = make_state(
        high_confidence=1,
        own_tracked_alt_rate=100,
        current_vertical_sep=700,
        other_capability=0,
        own_tracked_altitude=0,
        other_tracked_altitude=1000,  # own below threat
        up_separation=1000,
        down_separation=0,
        altitude_layer_value=0,
    )
    # expect upward RA -> 1
    assert altitude_separation_test(s) == 1


def test_need_downward_RA():
    # construct a state where downward RA is required
    s = make_state(
        high_confidence=1,
        own_tracked_alt_rate=100,
        current_vertical_sep=700,
        other_capability=0,
        own_tracked_altitude=1000,
        other_tracked_altitude=0,  # own above threat
        up_separation=200,
        down_separation=200,
        positive_ra_alt_thresh_0=100,
        altitude_layer_value=0,
    )
    # expect downward RA -> 2
    assert altitude_separation_test(s) == 2


def test_both_need_up_and_down():
    # contrive state where both up and down computed True (leads to 0)
    s = make_state(
        high_confidence=1,
        own_tracked_alt_rate=100,
        current_vertical_sep=700,
        other_capability=0,
        own_tracked_altitude=0,
        other_tracked_altitude=1000,
        up_separation=1000,
        down_separation=1000,
        altitude_layer_value=0,
    )
    # both True -> alt_sep = 0 per code
    assert altitude_separation_test(s) == 0
