# TCAS Test Report

1) Fork link

- Fork URL: https://github.com/1izh4n/tcas

2) Predicates (decision statements) identified

- Top-level precondition in `altitude_separation_test`:
  - `state.high_confidence`
  - `state.own_tracked_alt_rate <= 600`
  - `state.current_vertical_sep > 600`
  - `state.other_capability == 1`
  - `state.two_of_three_reports_valid`
  - `state.other_rac == 0`
  - combined as: (A and B and C) and ((D and (E and F)) or not D)
- `non_crossing_biased_climb` and `non_crossing_biased_descend` each contain an
  `if inhibit_biased_climb(state) > state.down_separation:` decision and
  compound boolean expressions using `own_below_threat`, `own_above_threat`,
  comparisons with `alim(state)`, and separations.
- `positive_ra_alt_thresh` has an `if/elif` ladder over `layer`.

3) Is predicate (branch) coverage possible? What was challenging?

- Yes. Predicate coverage is achievable for many branches. I implemented a predicate-based suite that exercises the major branches and RA outcomes.
- Challenges:
  - Several branches depend on numeric thresholds and layered thresholds
    (`alim`) with large defaults; constructing inputs to hit desired branches
    required tuning `up_separation`, `down_separation`, and the
    `positive_ra_alt_thresh_*` fields.

4) Is active-clause (MCDC) coverage possible? What was challenging?

- Partially. These tests show that toggling a single atomic clause can
  change the decision outcome while keeping others fixed in several cases.
- Challenges:
  - The boolean structure includes sub-expressions like `(D and (E and F)) or
    not D`, which make it non-trivial to find assignments where toggling one
    clause alone flips the predicate while all other clauses remain fixed.


5) Which one gives more confidence?

   Predicate/branch tests. Because they are straightforward, and ensure that each sides of
  each decision can be executed. They provide good confidence that code paths behave as expected for chosen inputs.

6) Branch-coverage scores

- Running the full test suite (predicate + clause + original) produced:
  - overall branch-rate: 69.23%
  - `src/tcas/main.py` branch-rate: 66.67%
- Predicate-only tests (`test/predicate`) produced:
  - overall branch-rate: 61.54%
  - `src/tcas/main.py` branch-rate: 58.33%
- Clause-only tests (`test/clause`) produced:
  - overall branch-rate: 42.31%
  - `src/tcas/main.py` branch-rate: 37.50%

