# Copyright 2026 Gerard Ando
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Command line simulation and independent-data analysis."""
import argparse
import json
from pathlib import Path
from .simulation import simulate
from .analysis import analyze_trial


def main():
    parser = argparse.ArgumentParser(description="Thermal research tools; no hardware IO")
    sub = parser.add_subparsers(dest="command", required=True)
    sim = sub.add_parser("simulate")
    sim.add_argument("--mass-g", type=float, default=500)
    sim.add_argument("--start-c", type=float, default=20)
    sim.add_argument("--target-c", type=float, default=40)
    sim.add_argument("--output", type=Path, required=True)
    analysis = sub.add_parser("analyze")
    analysis.add_argument("input", type=Path)
    analysis.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == "simulate":
            result = simulate(args.mass_g, args.start_c, args.target_c)
        else:
            result = analyze_trial(json.loads(args.input.read_text()))
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")
    except (ValueError, TypeError, KeyError, OSError) as exc:
        parser.exit(2, f"error: {exc}\n")
    print(f"Wrote {args.output}")
    if args.command == "analyze" and not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
