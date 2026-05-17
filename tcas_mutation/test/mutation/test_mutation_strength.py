import pytest

from tcas.main import (
    alim,
    altitude_separation_test,
    inhibit_biased_climb,
    non_crossing_biased_climb,
    non_crossing_biased_descend,
    own_above_threat,
    own_below_threat,
    positive_ra_alt_thresh,
)
from tcas.state import State


def make_state(**kwargs) -> State:
    defaults = dict(
        current_vertical_sep=700,
        high_confidence=1,
        two_of_three_reports_valid=1,
        own_tracked_altitude=0,
        own_tracked_alt_rate=100,
        other_tracked_altitude=1000,
        altitude_layer_value=0,
        up_separation=500,
        down_separation=100,
        other_rac=0,
        other_capability=1,
        climb_inhibit=0,
        positive_ra_alt_thresh_0=100,
        positive_ra_alt_thresh_1=200,
        positive_ra_alt_thresh_2=300,
        positive_ra_alt_thresh_3=400,
    )
    defaults.update(kwargs)
    return State(**defaults)


def test_threat_helpers_are_strict():
    equal = make_state(own_tracked_altitude=1000, other_tracked_altitude=1000)
    below = make_state(own_tracked_altitude=999, other_tracked_altitude=1000)
    above = make_state(own_tracked_altitude=1001, other_tracked_altitude=1000)

    assert own_below_threat(equal) is False
    assert own_above_threat(equal) is False
    assert own_below_threat(below) is True
    assert own_above_threat(below) is False
    assert own_below_threat(above) is False
    assert own_above_threat(above) is True


@pytest.mark.parametrize(
    ("layer", "expected"),
    [(-1, 0), (0, 100), (1, 200), (2, 300), (3, 400), (4, 0)],
)
def test_positive_ra_alt_thresh_selects_exact_layer(layer, expected):
    assert positive_ra_alt_thresh(make_state(), layer) == expected


@pytest.mark.parametrize(("layer", "expected"), [(0, 100), (1, 200), (2, 300), (3, 400)])
def test_alim_uses_state_altitude_layer(layer, expected):
    assert alim(make_state(altitude_layer_value=layer)) == expected


def test_inhibit_biased_climb_adds_exact_bias_only_when_enabled():
    assert inhibit_biased_climb(make_state(up_separation=500, climb_inhibit=0)) == 500
    assert inhibit_biased_climb(make_state(up_separation=500, climb_inhibit=1)) == 600


def test_non_crossing_biased_climb_first_branch_boundary_at_alim():
    base = dict(
        own_tracked_altitude=0,
        other_tracked_altitude=1000,
        up_separation=501,
        down_separation=500,
        positive_ra_alt_thresh_0=500,
    )
    assert non_crossing_biased_climb(make_state(**base)) is False
    assert non_crossing_biased_climb(make_state(**{**base, "down_separation": 499})) is True


def test_non_crossing_biased_climb_second_branch_vertical_and_up_boundaries():
    base = dict(
        own_tracked_altitude=1000,
        other_tracked_altitude=0,
        up_separation=500,
        down_separation=501,
        positive_ra_alt_thresh_0=500,
    )
    assert non_crossing_biased_climb(make_state(**base, current_vertical_sep=300)) is True
    assert non_crossing_biased_climb(make_state(**base, current_vertical_sep=299)) is False
    assert non_crossing_biased_climb(make_state(**{**base, "up_separation": 499})) is False


def test_non_crossing_biased_descend_first_branch_boundaries():
    base = dict(
        own_tracked_altitude=0,
        other_tracked_altitude=1000,
        up_separation=501,
        down_separation=500,
        positive_ra_alt_thresh_0=500,
    )
    assert non_crossing_biased_descend(make_state(**base, current_vertical_sep=300)) is True
    assert non_crossing_biased_descend(make_state(**base, current_vertical_sep=299)) is False
    assert non_crossing_biased_descend(make_state(**{**base, "down_separation": 499})) is False


def test_non_crossing_biased_descend_second_branch_boundary_at_alim():
    base = dict(
        own_tracked_altitude=1000,
        other_tracked_altitude=0,
        up_separation=500,
        down_separation=501,
        positive_ra_alt_thresh_0=500,
    )
    assert non_crossing_biased_descend(make_state(**base)) is True
    assert non_crossing_biased_descend(make_state(**{**base, "up_separation": 499})) is False


@pytest.mark.parametrize(
    ("kwargs", "expected"),
    [
        (dict(own_tracked_alt_rate=600), 1),
        (dict(own_tracked_alt_rate=601), 0),
        (dict(current_vertical_sep=601), 1),
        (dict(current_vertical_sep=600), 0),
        (dict(other_capability=1, two_of_three_reports_valid=1, other_rac=0), 1),
        (dict(other_capability=1, two_of_three_reports_valid=0, other_rac=0), 0),
        (dict(other_capability=1, two_of_three_reports_valid=1, other_rac=1), 0),
        (dict(other_capability=0, two_of_three_reports_valid=0, other_rac=1), 1),
    ],
)
def test_altitude_separation_top_level_boundaries(kwargs, expected):
    advisory_state = make_state(down_separation=99, **kwargs)
    assert altitude_separation_test(advisory_state) == expected


def test_altitude_separation_returns_downward_and_no_advisory_cases():
    downward = make_state(
        own_tracked_altitude=1000,
        other_tracked_altitude=0,
        up_separation=500,
        down_separation=501,
        positive_ra_alt_thresh_0=500,
    )
    no_advisory = make_state(
        own_tracked_altitude=0,
        other_tracked_altitude=1000,
        up_separation=500,
        down_separation=500,
        positive_ra_alt_thresh_0=500,
    )

    assert altitude_separation_test(downward) == 2
    assert altitude_separation_test(no_advisory) == 0
