# Development guide

Use Python 3.10+. The runtime uses only the standard library. Run from the repository root with `PYTHONPATH=src`, or optionally install using `python -m pip install -e .` in an isolated environment. Installation may need network access for build tooling.

## Tests

Run `PYTHONPATH=src python -m unittest discover -s tests -v`. Tests cover state transitions, mutual exclusion, dwell reset, fault latching, invalid configuration, timeouts, the 12-cell synthetic thermal matrix and independent-reference analysis. Passing tests establish software behavior against these cases; they do not qualify hardware.

## Commands

`simulate` accepts a declared mass, start temperature, target and output path. JSON includes provenance, model description, elapsed time and per-second samples. Thermal and electrical rates are assumed constants stated in source.

`analyze` reads the normalized independent-reference format in DATA_FORMAT.md. It exits 0 for a passing trial, 1 for a complete failing trial and 2 for invalid input or IO failure. It does not aggregate the 60-trial campaign or establish calibration validity; the reviewer must also apply cell-level acceptance and confidence intervals from the protocol.

## Rebuilding proposal documents

Install optional document dependencies with `python -m pip install -e '.[documents]'`. Run `python tools/build_proposals.py --output-dir local-results/proposals`. The generator writes Markdown, two PDFs, JSON templates and a document archive into the selected output area. It does not modify the canonical documents automatically. Compare regenerated files, render PDFs and review layout before replacing committed artifacts. The generator preserves the proposal version date; changing it requires an explicit content revision.

## Change discipline

Add tests when changing failure behavior or validation rules. Keep synthetic examples separate from real measurements. Assign hardware and firmware revisions to every future test campaign. Do not tune on final validation data. Check instructions against clean CLI runs before release.
