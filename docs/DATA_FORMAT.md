# Independent measurement data format

The earlier proposal's Test_Log_Template.json is a human planning template. The analyzer uses the normalized schema below; it does not parse that planning template directly.

Required top-level fields: `provenance` equal to `measured`, `target_c` from 20 through 60, nonnegative `expanded_uncertainty_c`, `completion_s`, three distinct `reference_sensor_ids`, and ordered `samples`. Completion is relative to cycle start. Optional `trial_id` identifies the trial.

Each sample has `timestamp_s` and exactly three finite `reference_c` values. Timestamps must strictly increase. The completion window includes both completion minus 60 seconds and completion itself, with at least 61 records and no gap above one second. The uncertainty input must come from an approved budget; the software does not infer it.

Pass requires all window values plus uncertainty to fit inside +/-1 C, spatial range <=2 C and completion before 1800 seconds. Missing data is invalid and must count as a campaign failure under the protocol unless an approved external interruption rule applies. Errors must not disappear from the trial ledger because analysis rejected them.

`examples/analysis_format_fixture.json` is a fabricated schema demonstration, not experimental evidence. Its label exists only to exercise the parser. Simulation outputs deliberately have a different schema and provenance and are rejected by this analyzer.

Retain raw instrument exports alongside normalized records, calibration documents, conversion scripts, hashes, revision identifiers and deviations. Do not overwrite instrument exports. Store real participant contact records separately and privately. Never commit personal or sensitive pilot data to this public repository.
