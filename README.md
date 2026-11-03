# THERMA COMMONS

Precision heating and cooling research platform led by Gerard Ando (JD).

This repository brings together the 20-concept platform proposal, sponsorship materials, experimental protocols and a runnable research software starter. **Status: concept-stage feasibility.** No physical prototype, food-safety validation, patent clearance, certification or sponsorship commitment is represented.

## Start here

- [Executive brief](docs/proposals/01_Executive_Brief.md)
- [Master proposal and all 20 concepts](docs/proposals/02_Master_Proposal.md)
- [Complete proposal PDF](artifacts/THERMA_COMMONS_Complete_Proposal.pdf)
- [Executive brief PDF](artifacts/THERMA_COMMONS_Executive_Brief.pdf)
- [All 15 proposal documents](docs/proposals/00_Start_Here.md)
- [Developer guide](docs/DEVELOPMENT.md)
- [Software architecture](docs/SOFTWARE_ARCHITECTURE.md)
- [Data format](docs/DATA_FORMAT.md)
- [Hardware development plan](docs/HARDWARE_PLAN.md)
- [Preliminary BOM](docs/PRELIMINARY_BOM.md)
- [Roadmap](docs/ROADMAP.md)
- [Publication and IP status](RIGHTS.md)

## Partner execution and outreach

[Research and recommended sequence](docs/outreach/EXECUTION_RESEARCH.md) | [Verified contact register](docs/outreach/CONTACT_REGISTER.md) | [12 tailored drafts](docs/outreach/drafts/) | [Supplier and metrology RFQ](docs/outreach/MODULE_AND_METROLOGY_RFQ.md) | [Complete contact package PDF](artifacts/outreach/THERMA_COMMONS_Contacts_and_Execution.pdf)

Public contacts and capabilities were researched on November 2, 2026. Drafts have not been sent. No provider has committed access, funding, pricing or a paid pilot. The existing universal proposal documents remain sponsor-neutral.

## Run without third-party dependencies

Python 3.10 or later:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python -m therma_commons.cli simulate --mass-g 500 --start-c 60 --target-c 40 --output local-results/cooling.json
PYTHONPATH=src python -m therma_commons.cli analyze examples/analysis_format_fixture.json --output local-results/analysis.json
```

The analysis-format fixture is fabricated solely to demonstrate the parser. Its `measured` label exercises the input contract; it is not a real measured dataset and cannot support a performance claim. Do not submit it as evidence.

Simulation results are visibly labeled synthetic. The model assumes well-mixed water and fixed thermal parameters. It cannot predict arbitrary food temperatures. The controller provides software state transitions only: **there are no GPIO, mains, refrigeration or RF drivers**. A simulated READY state refers to its control channel, not independent temperature verification or food safety.

## Proposed program

The opening request is $25,000 for a 12-week liquid-demonstrator feasibility study, plus optional separately valued in-kind support. All costs and metrics are planning assumptions. Target +/-1 C performance is unachieved. Gate decisions, independent measurements and customer evidence determine whether later tray, paired-chamber, luxury and community variants proceed.

## Licensing

The research software in `src/` and `tests/`, together with `pyproject.toml` and `.github/workflows/`, is licensed under the [Mozilla Public License 2.0](LICENSE). Commercial use is permitted without a royalty obligation under MPL; when covered files are distributed with modifications, MPL source-availability obligations apply. Separate proprietary files can be combined into larger works under the license conditions.

Proposal documents, PDFs, archives, example data, the proposal-generation tool and other materials remain reserved unless separately licensed. See [RIGHTS.md](RIGHTS.md) for the precise scope, limited patent grants, contributor terms and commercial-rights boundaries. The open-source component is the research software; the entire repository is not under one open-source license.

## Repository map

`src/` research source; `tests/` deterministic tests; `docs/proposals/` 15 editable documents; `docs/` implementation and diligence guides; `examples/` budgets and schemas; `artifacts/` rendered proposal PDFs and document archive; `tools/` reproducible document authoring source; `.github/workflows/` CI.

Core operations are offline. No personal data, credentials or real participant records are required. See [SECURITY.md](SECURITY.md). Contact: g.ando@gkitchen.in.
