from pathlib import Path
import json, zipfile, re, html
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from pypdf import PdfReader

import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--output-dir',type=Path,default=Path('local-results/proposals'))
ROOT=parser.parse_args().output_dir.resolve()
ROOT.mkdir(parents=True,exist_ok=True)
docs=[]
def add(name,title,body):
    text=f'# {title}\n\nTHERMA COMMONS | November 2, 2026 | Version 1.0\n\n'+body.strip()+'\n'
    (ROOT/(name+'.md')).write_text(text)
    docs.append((name,title,text))

add('00_Start_Here','Sponsorship package guide', '''
## Decision requested
Support a 12-week, stage-gated feasibility program for a precision heating and cooling platform. The recommended initial request is $25,000 in cash plus up to $10,000 of separately valued in-kind engineering, equipment access and independent testing. The first demonstrator handles stirred water and defined nonhazardous food simulants. It is not a consumer-ready microwave or a validated food-safety device.

## How to use this package
Send the Executive Brief first. Send the Master Proposal, Budget and Milestones after a partner expresses interest. Share the Technical Requirements and Validation Protocol with engineering reviewers. Use the Partnership Brief and Pilot Charter to agree on work before spending funds. Retain the IP and Risk documents for diligence and negotiations.

This package contains 15 editable Markdown documents, two presentation-ready PDFs, an editable JSON budget, a test-log template and a complete ZIP archive. The pitch narrative is a speaking outline rather than a slide deck. Legal instruments, regulatory submissions and patent filings require project-specific professional preparation; the included negotiation brief does not replace executed agreements.

## Current evidence status
Concept formulation only. No prototype, test data, incorporated entity, patent application, certifications, sales, partner commitments or confirmed team appointments are represented. Proposed metrics, budgets and timelines are planning assumptions. Founder and project lead: Gerard Ando, also known as JD. Contact: g.ando@gkitchen.in. Relevant engineering credentials and prior accomplishments must be verified before external use.

## Required fields before submission
Confirm applicant entity and address, entity eligibility, signatory, payment recipient, engineering lead, laboratory access, insurance and proposed project start. Confirm any program-specific format, deadline, geographic rules and eligible expenses separately. Do not invent missing registrations or organizational capacity.

## Document map
01 Executive Brief; 02 Master Proposal; 03 Technical Requirements; 04 Validation Protocol; 05 Budget and Milestones; 06 Partnership and Sponsorship Brief; 07 Pilot Charter; 08 Intellectual Property and Commercialization; 09 Risk and Compliance; 10 Impact and Access; 11 Outreach and Application Copy; 12 Pitch Narrative and Questions; 13 Evidence Register; 14 Execution and Data Room.

## Recommended first action
Use a nonconfidential brief to recruit one thermal-controls engineering reviewer and one independent measurement partner. Seek written scoping feedback on the liquid demonstrator before requesting funding for an integrated RF appliance. No outreach has been sent and no agreements have been executed.
''')

add('01_Executive_Brief','Precision heating and cooling executive brief', '''
## The proposal
THERMA COMMONS is a proposed modular appliance platform that heats, actively cools and verifies temperature for defined food and beverage loads. We seek $25,000 for a 12-week feasibility program, with an optional $10,000 in-kind contribution. The program will establish whether a cleanable stirred-vessel demonstrator can reach a selected temperature reproducibly and with practical time and energy use.

## The problem and insight
Users commonly specify cooking time while actually wanting a temperature outcome. Heating can leave uneven temperatures; cooling often requires waiting, transfer or improvised handling. The useful opportunity is verified control of the full thermal journey. A surface reading or precise display alone does not establish internal food temperature.

## The initial solution
A removable food-compatible vessel sits in a heating and cooling dock. Mixing reduces gradients. A control sensor and an independent reference measurement establish endpoint performance. The controller approaches a selected target, checks stability and reports measured versus unverified status. The first experiments use water and defined simulants; raw-food cooking and microbiological claims are excluded.

## The larger platform
After feasibility, the architecture extends to shallow meal trays, paired cooking and chilling chambers, accessible controls, heat recovery when useful, reusable thermal storage, repairable modules and community-kitchen variants. Solid-state RF and unconventional refrigeration remain optional research tracks. Bespoke luxury finishes and quieter packaging follow functional proof.

## Twelve-week evidence deliverables
Requirements and hazard review; reference-calibrated bench demonstrator; a randomized validation dataset; endpoint, gradient, time and wall-energy results; cleaning assessment; failure-injection results; an independent review; and a costed next-stage decision. Primary target: at least 95 percent of final blinded water trials within +/-1 degree C of the selected target under a declared operating envelope. This is a development target, not achieved performance or a food-safety guarantee.

## What a partner receives
A defined statement of work, milestone reports, agreed attribution, a demonstration and access to agreed nonconfidential results. Intellectual property, publication and licensing rights are negotiated separately. Sponsorship does not automatically grant equity, exclusivity, certification or patent ownership.

## Why this approach can move faster
Start with one measurable task using established heating and refrigeration components. Spend first on measurement, controls and cleanability. Release funding in stages. Expand only when evidence supports the next level of complexity.

## Project contact
Gerard Ando | Project lead | g.ando@gkitchen.in. Project status: concept-stage; specialist engineering collaborators sought. The working name is subject to trademark clearance.
''')

add('02_Master_Proposal','Master proposal for a modular precision thermal platform', '''
## Purpose and central proposition
We propose one shared thermal-control platform with several products and an explicitly bounded research program. Its purpose is to reduce uncertainty between a user's chosen temperature and the actual state of a defined food or beverage. The core combines active heating, active cooling, suitable sensing, a cleanable vessel interface and a controller that communicates its measurement limits.

The requested decision is to fund a small feasibility program before committing to integrated RF hardware, industrial design or broad food claims. The proposed 12-week cash budget is $25,000; optional in-kind support is tracked separately. Later-stage figures are illustrative allowances rather than approved budgets or quotations.

## Problem definition
Existing appliances offer substantial heating, sensing, refrigeration and culinary capabilities. The remaining hypothesis is that users will value an easier, verified transition between heating, cooling and serving. The project does not assume that all existing products lack temperature control. Customer discovery and comparative testing must establish which unmet workflow deserves a product.

Three temperatures must remain distinct: the cooking endpoint, the immediate serving target and the refrigerated-storage endpoint. A pleasant serving temperature is not evidence of a safe cooking process. Food can also contain multiple temperatures simultaneously. Verification must specify sensor location, food geometry, uncertainty and acceptable gradients.

## Unified architecture
The platform has five common elements: a removable load interface, thermal actuators, calibrated sensing, deterministic supervisory controls and a human interface. A sixth optional element captures operational data locally with explicit export consent. The safety controller must remain functional without cloud connectivity or a learned model.

The phase-one vessel uses contact heating, a qualified cooling module and mixing. A paired-chamber product can later add an independently engineered microwave or RF cooking chamber beside a refrigeration chamber. Separate chambers reduce thermal conflict and make drainage and cleaning easier to design. They also increase size and transfer effort; user testing must quantify the tradeoff.

## Integration of all twenty concepts
1. Verified serve-temperature station becomes the common outcome-control architecture.
2. Precision beverage dock becomes the first physical demonstrator and possible entry product.
3. Twin-chamber atelier becomes the premium integrated appliance configuration.
4. Adaptive RF becomes an optional heating-engine research workstream after baseline proof.
5. Measured meal tray becomes a documented vessel and sensing interface.
6. Independent meal zones become physically separated modules, not unsupported spatial RF promises.
7. Heat recovery becomes an optional coupling between useful hot and cold loads.
8. Affordable temperature finisher becomes a cooling-only derivative for existing kitchens.
9. Stir-and-serve bowl supplies the initial controllable food geometry.
10. Leftover chiller becomes a later validated storage-cooling workflow.
11. Thaw-to-cook becomes a later food-specific program requiring separate safety validation.
12. Steam, RF and crisping become optional culinary modules rather than phase-one requirements.
13. Accessible concierge becomes a shared user-interface requirement across versions.
14. Care-meal assistant becomes a supervised application needing additional safeguards.
15. Thermal-storage cartridge becomes an alternative cooling accessory with full charging-energy accounting.
16. Grid-flexible pantry becomes an energy-management feature that cannot override food constraints.
17. Repairable platform becomes a shared service architecture with qualified safety-critical repair.
18. Community hub becomes a commercial variant with its own sanitation and duty-cycle requirements.
19. Vacuum cooling becomes an isolated specialist research track for appropriate foods.
20. Solid-state cooling becomes a research option benchmarked against compressor refrigeration.

## Product family and sequencing
The first offer is a precision beverage and soup dock. The second is a cooling finisher and standardized shallow-tray system. The third is a paired heating and chilling appliance. A luxury edition adds finish quality, acoustic treatment and personal configuration after performance and serviceability are proven. A community version prioritizes throughput, accessibility and local service. A low-cost edition retains temperature transparency and essential protections; it does not receive weaker safety controls.

## Research hypotheses
H1: Controlled mixing and a known vessel allow repeatable endpoint performance within a stated tolerance. H2: The full workflow improves user-rated convenience against ordinary heating and cooling. H3: Cleaning can be completed without inaccessible food residue. H4: Added active cooling is worth its energy, noise, cost and footprint for a defined market. H5: Shared modules reduce derivative development cost without introducing unacceptable compromises. Each hypothesis can fail independently.

## Initial scope and exclusions
Initial loads are 250, 500 and 750 grams of water and later declared simulants, in one vessel geometry at normal indoor conditions. Initial targets are 20, 40 and 60 degrees C where the starting conditions permit the required heating or cooling test. These engineering tests do not validate food safety, infant feeding, medical uses, raw animal products or unrestricted unattended operation. Human consumption is outside initial bench testing.

## Differentiation and defensibility
Potential differentiation lies in validated endpoint control, thermal-transition design, a hygienic vessel interface, interpretable uncertainty and affordable serviceable derivatives. RF cooking, blast chilling and low-temperature cooking already exist [S3-S4]. Patent novelty and freedom to operate are unresolved. An implementation, dataset or interface can be commercially useful without a broad hardware patent.

## Program and decision gates
Weeks 1-2 define requirements, hazards, measurement uncertainty and purchase specifications. Weeks 3-5 assemble the rig and establish control. Weeks 6-8 tune on a development dataset. Weeks 9-10 run a locked, blinded validation protocol. Weeks 11-12 complete independent review, cleanability assessment, customer interviews and a next-stage recommendation. Failed validation triggers a bounded correction plan or stop decision; it does not justify relabeling the target.

## Benefits and evidence discipline
The project aims to reduce unnecessary waiting and overheating, make uncertainty visible and enable user preference without confusing it with food safety. Reduced food waste, nutrient retention, lower energy use and better safety are hypotheses requiring different evidence. Thermal accuracy alone proves none of them. Public reporting should distinguish targets, measurements, interpretation and independently reviewed findings.

## Partnership request and governance
We seek thermal-control expertise, measurement access, qualified refrigeration integration and milestone-based funding. Gerard Ando is the project lead; engineering, food-science and commercialization roles remain to be filled. One technical reviewer should be independent of the person building the controller. Weekly reviews track scope, spend, hazards and decisions. Changes to the test envelope require versioned approval before final validation.

## Commercial path
Preferred order is paid feasibility work or sponsored prototyping, a defined co-development pilot, then licensing or manufacturing partnership if evidence supports demand. Licensing may reduce manufacturing capital needs but sacrifices control and a share of revenue. Direct manufacturing gives more control but adds certification, inventory, warranty and service obligations. No royalty rate or commercial return is promised.

## Conclusion and requested next step
Authorize the first gate: confirm the engineering team, approve the measurement protocol and release the first $5,000 against a signed work plan. The near-term asset is credible evidence for one useful thermal task. The platform grows only when that evidence supports expansion.
''')

add('03_Technical_Requirements','Technical architecture and preliminary requirements', '''
## Intended engineering scope
This document defines the first stirred-liquid demonstrator and the interfaces needed for a later platform. All values are proposed requirements subject to engineering review. A requirements freeze precedes validation.

## Functional requirements
R01: Accept one specified removable vessel with declared maximum fill and minimum immersion depth. Detect missing or incorrectly seated vessels before actuation.
R02: Accept 250, 500 and 750 gram water loads with mass recorded on an independent scale. Begin validation at 20 +/-2 degrees C ambient.
R03: Provide heating and active cooling in a prototype target range of 20 to 60 degrees C. The engineering lead must approve limits before operation. No freezing, pressure operation or raw-food cooking in phase one.
R04: Record selected target, starting temperatures, sensor locations, firmware version, start and stop times, wall energy and completion status.
R05: Target +/-1 degree C endpoint error for at least 95 percent of final blinded water trials. Setpoint entry resolution must not be advertised as accuracy.
R06: Require 60 seconds within the endpoint band with reference-observed spatial range no greater than 2 degrees C before a trial can pass. This assesses defined liquids only.
R07: Detect control-sensor faults, abnormal temperature rise, dry heating, blocked mixing and abnormal cooling conditions. Stop relevant actuation and show a specific fault.
R08: An independent overtemperature limiter and hardware power isolation must protect against a failed main controller. Cooling faults must also stop or limit operation as appropriate.
R09: Core operation and local logs remain available offline. No personal data or audio recording is required.
R10: Food-contact components must be removable and visibly inspectable. Drainage must prevent condensate from reaching electrical components or standing in inaccessible cavities.

## Physical architecture
Power inlet and protection feed separately controlled heating and refrigeration subsystems. A mains-rated, reviewed switching stage sits outside the wet zone. A low-voltage controller reads a calibrated control sensor, load-state inputs and fault signals. An independent logger reads at least three reference points through a separate measurement chain. A removable stirrer is isolated from electrical and entanglement hazards.

Heating and cooling are mutually scheduled in phase one; simultaneous antagonistic operation is disabled. A sealed secondary cooling circuit can isolate the refrigeration assembly from food. Thermal coupling, leak detection and condensate handling need explicit design review. Do not modify a consumer microwave or bypass its interlocks for these tests.

## Control state sequence
Idle -> load check -> sensor plausibility -> heat or cool -> approach target -> equalize -> verify -> ready for immediate use or test completion. A fault transitions to actuation disabled and an instruction to inspect. Power restoration requires a fresh load and process review rather than blindly resuming. The controller must not label a process food-safe based on this sequence.

## Measurement uncertainty
Budget reference calibration uncertainty, resolution, drift, immersion, response lag, spatial gradients and logger synchronization separately. Prefer a reference expanded uncertainty of at most 0.3 degree C over the tested range, to be established rather than assumed. Use a decision guard band: endpoint error plus applicable expanded measurement uncertainty must fit within the claimed tolerance. If that cannot be achieved, loosen and clearly restate the claim before testing.

## Preliminary component classes
One removable vessel and lid; one controlled contact heater; one reviewed compressor cooling assembly with secondary loop; pump and heat exchanger; insulated tubing; removable stirrer; control sensor; independent reference sensors and logger; independent thermal cutoff; controller and interface; power meter; scale; enclosure and drip containment; approved switches, fuses and wiring; cleaning tools. Selection requires ratings, material compatibility and actual quotations. No specific part is prequalified by this document.

## Later interfaces
Document vessel geometry, permissible materials, thermal contact, cleaning requirements and identification format. RF compatibility must be assessed separately; a metal vessel suitable for this dock must not be assumed safe in a microwave. RF modules require independent cavity, interlock, leakage, EMC and thermal analysis. Consumer and commercial variants receive separate requirements baselines.

## Design tradeoffs
Compressor cooling offers a practical baseline but introduces sound, refrigerant and service needs. Thermoelectrics can simplify a small demonstrator but must be benchmarked for useful heat-removal rate and whole-cycle energy before product selection. Thermal storage shifts energy in time and has finite capacity. No cooling option removes the internal conduction limit in thick foods.
''')

add('04_Validation_Protocol','Measurement validation and experimental protocol', '''
## Objective and permitted inference
Determine repeatability, endpoint error, spatial variation, completion time and wall energy for defined water loads. A successful result supports only the declared test envelope. It does not establish pathogen reduction, shelf life, nutrient preservation or general food safety.

## Equipment and preparation
Assign a qualified test owner and separate reviewer. Use the approved vessel, an independent mass scale, a wall-energy meter and three reference temperature channels. Record calibration certificates or comparison results, uncertainty, sensor serial numbers and expiration. Check sensors before and after the campaign at documented points spanning the operating range. Do not rely on the control sensor as the sole truth measurement.

## Test matrix
Use three masses: 250, 500 and 750 grams. Use four transitions: 20 to 40 degrees C, 20 to 60 degrees C, 60 to 40 degrees C and 40 to 20 degrees C. Run five repeats per cell: 3 x 4 x 5 = 60 final trials. Reference starting temperature tolerance is +/-1 degree C. Ambient is 20 +/-2 degrees C. Record actual humidity and mains voltage where available. Predefine a maximum cycle time of 30 minutes per trial; report timeouts as failures. This is a provisional feasibility limit, not a consumer performance promise.

## Development and blinding
Use a separate tuning dataset, not part of the 60 final trials. Freeze hardware, firmware, sensor placement and analysis code before final runs. Randomize cell order using a recorded seed. Where practical, keep the controller operator unaware of independent reference readings. An independent reviewer receives raw logs and the frozen acceptance rules.

## Trial procedure
Inspect the vessel and wet zone. Weigh the water. Position reference sensors at defined central, near-wall and upper positions, away from direct contact with the heater and stirrer. Establish starting conditions and record at 1 Hz or faster using synchronized timestamps. Run the selected transition. At reported completion, record 60 seconds of reference readings. Note peak overshoot, minimum temperature, interruptions and visual observations. Clean, reset and document deviations before the next run.

## Pass rules
For a completed trial, the uncertainty-adjusted error of every reference channel must stay inside +/-1 degree C throughout the final 60 seconds, and the simultaneous spatial range must remain at or below 2 degrees C. At least 57 of 60 trials must pass, with no matrix cell below 4 of 5. Report both aggregate and cell results. A 57-of-60 result is preliminary evidence with sampling uncertainty, not proof of a 95 percent population success rate. Report an exact binomial or Wilson confidence interval.

## Failure and missing-data rules
Timeouts, uncommanded restarts, missing reference records or sensor disagreement that prevents verification count as failures. A documented external interruption may be reported separately, with the original result retained and one labeled replacement trial. Never discard inconvenient results or retune the controller during the final campaign. After changes, assign a new version and repeat the affected validation matrix.

## Comparator
Measure the same load transitions using a conventional heat source and a defined passive or ice-bath cooling workflow as applicable. Include transfers, stirring, waiting, preconditioning and allocated thermal-storage charging energy. At least three comparator repeats per cell provide a directional baseline. Do not claim superiority from these small trials without an appropriate comparison design and uncertainty analysis.

## Fault and hygiene tests
Under engineering supervision, inject sensor disconnection, implausible readings, stalled mixing, empty vessel, obstructed cooling airflow and power interruption. Predetermine the allowed response time for each fault from the hazard analysis. Do not short mains circuits or defeat protections. Test visible access, disassembly, reassembly and drainage after at least 20 cleaning cycles. A later food-contact hygiene assessment must be developed with a specialist.

## Reporting
Publish load and ambient conditions, all trial outcomes, mean and maximum errors, gradients, completion-time distributions, wall energy, uncertainty budget, fault responses and limitations. Retain raw data, calibration records, version hashes and deviations. No user study consumes bench-test material.

## Future food protocol
Validate foods separately by composition, thickness, initial state and intended use. Use multiple internal measurements, food-specific process requirements and a qualified food scientist. Microbiological studies require an appropriate laboratory. Care settings, infant feeding and vulnerable users need a separately approved risk and usability program before any claim or deployment.
''')

add('05_Budget_and_Milestones','Feasibility budget and stage gates', '''
## Funding structure
Recommended cash request: $25,000. Optional in-kind target: up to $10,000, separately valued and never added to cash receipts. All figures are USD planning allowances, not supplier quotations. The budget assumes a tightly scoped bench program with fractional specialist time and hosted workspace. It excludes a founder salary, full-time staff, production tooling, certification campaigns, patent filings, travel and a commercial launch. Taxes and shipping must fit within the stated allowances or trigger a documented revision.

## Cash budget
Thermal hardware and fabrication: $4,000. Sensors, logging and calibration: $2,500. Controls, electrical protection and enclosure: $2,000. Specialist thermal and controls engineering: $6,000. Independent testing and review: $2,500. Consumables and cleaning assessment: $1,000. Customer discovery and accessibility review: $1,000. Project coordination and documentation: $2,000. Subtotal: $21,000. Contingency: $4,000. Total: $25,000.

Engineering allowance assumes 60 hours at $100 per hour; independent review assumes 25 hours at $100 per hour; coordination assumes 40 hours at $50 per hour. These are modeling assumptions, not accepted contractor rates. If scope cannot fit this capacity, reduce deliverables or secure additional support before promising completion.

## Optional in-kind allocation
Up to $4,000 laboratory and metrology access; $3,000 specialist mentoring; $2,000 equipment loans; $1,000 prototype materials. Obtain a written contribution description, availability dates, valuation method, ownership and return obligations. Loan value is usage value, not the equipment's full purchase price. An unavailable in-kind dependency must be replaced or removed from scope.

## Gates and proposed cash releases
Gate A, weeks 1-2, $5,000: approved scope, hazard register, measurement plan, named technical owner and purchase list. Stop if appropriate oversight or a safe test site cannot be secured.
Gate B, weeks 3-5, $8,000: assembled rig, basic heating and cooling, independent logs and functional protective controls. Stop if a credible path to measurement or safe operation is absent.
Gate C, weeks 6-10, $8,000: frozen design, development data, 60-trial validation campaign and comparator measurements. Report failures without changing acceptance rules.
Gate D, weeks 11-12, $4,000: reviewed report, cleaning assessment, at least 12 discovery interviews targeted, updated costs and go/no-go recommendation. Interview completion is a target; recruitment and accessibility accommodations may change timing.

The gate figures total $25,000 including contingency. They are release ceilings, not a second expenditure budget. Contingency requires a recorded purpose and approval. Gate acceptance authorizes the next release but does not certify a product or guarantee a successful research outcome.

## Sensitivity
A 50 percent increase in the $6,000 engineering allowance consumes $3,000 of contingency, leaving $1,000. Replacing all $10,000 of expected in-kind support with cash increases total cash need to $35,000 if all optional work remains. A two-week delay can require a schedule extension and revised quotes; it is not assumed to be costless.

## Later planning envelopes
A 4-6 month defined-liquid and tray alpha might require $100,000-$250,000 after scoping. A 9-18 month paired-chamber development and precompliance program could require $500,000-$1.5 million or more, excluding broad rollout and inventory. These are rough order-of-magnitude decision allowances with low confidence, not fundraising commitments or validated industry averages.

## Financial controls
Track committed and actual cash separately, retain receipts, record donated resources separately and review burn weekly. Reallocation above $1,000 or a change to a required test needs written approval from the project lead and technical owner. Sponsor reporting must show cash balance, remaining commitments and the estimated cost to complete.
''')

add('06_Partnership_and_Sponsorship','Partner options and sponsorship statement of work', '''
## Preferred engagement
Begin with a nonexclusive, time-limited feasibility partnership. A modest funded experiment with clear evidence deliverables is the preferred fast route. Program speed depends on decision authority, contracting and equipment access, not on claims that a particular funding channel is automatically faster.

## Engagement options
Option A, technical review: a two-week scoped review with a proposed $1,500-$3,000 allowance, funded within Gate A rather than added automatically. Deliverable: written architecture and measurement critique.
Option B, full feasibility sponsorship: $25,000 cash over four gates. Deliverable: defined demonstrator, dataset and final report. Optional in-kind support is separate.
Option C, component or laboratory partnership: equipment loans, calibration access, thermal hardware or test time, capped by an agreed valuation. Deliverable: specific integration feedback and agreed acknowledgement.
Option D, paid co-development: a negotiated statement of work for the next validated application. Payment covers engineering; background and newly generated IP are explicitly allocated.
Option E, OEM evaluation license: limited evaluation rights after sufficient proof, with a separate option period and fee. Any future commercial license requires a new agreement.

## Statement of work
Objective: determine whether the defined liquid system meets frozen endpoint and measurement requirements. Work products: requirements baseline, hazard analysis, assembly description, controlled firmware version, raw logs, analysis, demonstrator review and recommended next stage. Acceptance concerns completeness and execution of the agreed experiments; meeting a research target cannot be guaranteed.

## Partner benefits
Agreed acknowledgement, milestone briefings, a supervised demonstration, a concise application-specific findings report and nonconfidential results access. Public logo use, press statements, testimonial language and any commercial rights require separate written approval. No sponsor receives an implied endorsement from a university, laboratory or regulator.

## Required commercial terms
Define parties, cash schedule, permitted costs, equipment ownership, return shipping, confidentiality exclusions, IP, publication review, records, insurance, site access, change control, termination, unused-fund treatment and dispute process. A proposed publication-review window is 30 days for confidential-information checks, with any patent-filing delay separately bounded. This is a negotiation position, not a signed commitment.

## Guardrails for faster collaboration
Use one authorized sponsor decision-maker and one technical counterpart. Separate evaluation access from long-term exclusivity. Avoid perpetual unpaid options, broad assignment of pre-existing ideas and milestone conditions outside the team's control. If exclusivity is requested, price its narrow field, geography, duration and minimum performance obligations.

## Partner selection scorecard
Score each candidate 0-5 for technical fit, resource availability, contracting speed, access to test users, IP fairness and service/manufacturing relevance. Weight technical fit and IP fairness twice. Maximum score: 40. Reject a high total if unsafe work practices or ownership demands are unacceptable. This is a decision tool, not a researched ranking of organizations.
''')

add('07_Pilot_Charter','Pilot charter and customer discovery plan', '''
## Pilot purpose
Identify a narrow customer workflow worth developing after bench feasibility. The first discovery segment is beverage and soup users in small hospitality or workplace settings. Household and care-setting uses are separate hypotheses. Do not mix their willingness to pay, duty cycles or risk requirements.

## Discovery before demonstration
Target 12 interviews across six operators, four household users and two accessibility reviewers. Ask for recent examples of cooling delays, reheating failures, cleaning burden and appliance service issues. Record task frequency, existing workaround, time cost, available counter space and purchasing authority. Do not present imagined savings as established facts.

## Interview questions
What happened the last time a drink or meal was too hot or uneven? What do you do now? How often does it occur? Who spends time correcting it? What temperature information do you trust? What would make this harder to clean? Where would it sit? What noise or cycle time is unacceptable? Who would approve a purchase? What would you stop buying to make room for it? Would you evaluate a defined prototype under supervision?

## Pilot prerequisites
Complete bench safety review and site-specific electrical and hygiene review. Sign a pilot agreement identifying the device status, allowed loads, supervisor, stopping rules, liability allocation and data permissions. Obtain appropriate insurance and participant consent. Do not expose users to consumable test food until the intended process, food-contact materials and hygiene controls are approved. Early usability work may use an unpowered mockup or water-only supervised demonstration.

## Proposed post-feasibility pilot
Up to two qualified sites, four weeks, one defined workflow per site. Assign one operator champion and one technical contact. Record task time, completion failures, cleaning time, noise perception, operator interventions, service incidents and stated willingness to pay. No unattended operation or use with vulnerable populations in this first pilot.

## Success and stop conditions
Proceed if users identify a repeated meaningful problem, the prototype meets its technical envelope and at least two qualified prospective evaluators agree to a documented next-stage evaluation. These are learning gates, not sales. Stop immediately after an electrical event, leak into the electrical zone, uncontrolled heating, failed protective function or unreviewed deviation. Preserve incident records and obtain clearance before restarting.

## Data and consent
Collect operational measurements without names where possible. Keep contact information separate. Participation is voluntary; record consent for quotations and images separately. Sponsor access is limited to agreed aggregate results unless participants explicitly authorize more. Do not gather medical histories in this pilot.

## Pilot closeout
Return or quarantine equipment as agreed. Reconcile incidents, clean and inspect the unit, document actual use and collect written feedback. Report negative findings and withdrawals. A letter of intent is not counted as revenue, a purchase order or product certification.
''')

add('08_IP_and_Commercialization','Intellectual property and commercialization brief', '''
## Commercial thesis
Build evidence for a reproducible thermal workflow and then choose between licensing, co-development and direct product delivery. The broad notion of heating and cooling is not presumed new. Defensibility may come from implementation details, cleanable interfaces, control performance, testing know-how and service quality.

## Disclosure sequence
Use the nonconfidential Executive Brief for first contact. Keep drawings, detailed control methods and unfiled potentially patentable implementations in a controlled annex. Record inventors' actual technical contributions and dates. Ask qualified patent counsel about disclosure consequences before public demonstration; treatment varies across jurisdictions. Do not label a concept patent-pending without a filed application.

## Prior-art and freedom-to-operate work
Search heating/cooling vessels, probe-guided appliances, RF feedback control, domestic blast chillers, thermal docking, multi-zone containers and temperature-finishing workflows. Record search date, databases, queries, patent families, legal status and claim relevance. Patentability and freedom to operate are separate questions. This package contains neither a patent opinion nor clearance.

## Ownership schedule to prepare
List background IP by contributor, project-generated inventions, firmware, datasets, drawings and third-party licenses. Contractor and institutional agreements must address ownership and permitted use before work begins. Maintain confidentiality and invention-assignment terms suitable to the actual relationship. Avoid assuming that payment alone transfers every right.

## Proposed licensing discussion points
Define field, territory, term, exclusivity, sublicense rights, development milestones, minimum commercialization effort, quality obligations, access rights, audit rights, termination and rights reversion. Define royalty base and deductions precisely. An illustrative royalty discussion can use a negotiated percentage of defined net sales, but no market rate or achievable rate is asserted here. Require counsel and financial review before agreeing.

## Route comparison
Paid feasibility work brings early project income and clearer scope, but may favor a partner-specific implementation. Licensing reduces manufacturing capital needs but introduces dependence on a licensee's execution and reporting. Joint development shares resources but needs careful IP and governance terms. Direct manufacturing provides control but adds inventory, certification, warranty, repair and working-capital exposure.

## Unit economics model
Net realized revenue = customer receipts less returns, discounts, taxes collected for authorities and channel deductions as applicable. Contribution = net realized revenue less landed hardware, assembly, quality checks, packaging, fulfillment, payment fees, warranty and variable support. Gross margin definitions vary; disclose included costs. Obtain actual supplier quotes at declared volumes before promising a retail price.

## Price sensitivity example
At a hypothetical $600 net realized revenue and $300 total variable cost, contribution is $300 before fixed costs. At $400 variable cost it falls to $200. With $150,000 fixed cost, those scenarios imply 500 or 750 units to cover that fixed cost, ignoring financing and timing. These are arithmetic examples, not forecasts, validated prices or a product-cost estimate.

## Brand and public language
THERMA COMMONS and THERMA Atelier are working names requiring clearance. Avoid universal exactness, guaranteed burn prevention, worldwide superiority, nutrient preservation and medical claims. A defensible early statement is: developing a platform to verify selected temperature outcomes for defined loads.
''')

add('09_Risk_and_Compliance','Risk register and compliance planning brief', '''
## Planning scope
This is an initial hazard and compliance planning document, not legal advice, approval or a complete conformity assessment. Product classification depends on intended use, market, electrical architecture, refrigeration and RF features. A qualified testing body and relevant specialists must confirm the applicable pathway before commercialization.

## Priority risks and controls
RISK 01 Uncontrolled heating: severity high; independent limiter, power isolation, dry-load detection and supervised fault tests. Owner: electrical lead, to be appointed.
RISK 02 False temperature confidence: severity high; independent references, uncertainty budget, multiple locations and clear measured/estimated labels. Owner: metrology lead, to be appointed.
RISK 03 Unsafe food process: severity high; separate cooking, serving and storage logic; initially exclude food-safety claims. Owner: food-science reviewer, to be appointed.
RISK 04 Liquid ingress and shock: severity high; isolated wet zone, drainage, suitable protective design and laboratory review. Owner: electrical lead.
RISK 05 Refrigeration fault or leak: severity high depending on refrigerant; qualified sealed assembly, ventilation and service procedures. Owner: refrigeration lead, to be appointed.
RISK 06 Cross-contamination: severity high; removable contact parts, cleaning validation and separation of raw and ready-to-eat workflows. Owner: hygiene reviewer, to be appointed.
RISK 07 Mixing entanglement or vessel breakage: severity medium-high; guarding, compatible materials, stop-on-open where required and misuse testing. Owner: mechanical lead, to be appointed.
RISK 08 RF leakage or arcing in later products: severity high; specialist design, cavity integrity, compatible vessels, interlocks and formal testing. Owner: future RF lead.
RISK 09 Unaffordable complexity: commercial impact high; constrained MVP, BOM reviews and stop gates. Owner: project lead.
RISK 10 Weak demand: commercial impact high; workflow interviews, comparator trials and conditional pilot commitments. Owner: project lead.
RISK 11 Excessive data collection: impact medium; offline defaults, minimal records, consent and deletion controls. Owner: software lead, to be appointed.
RISK 12 IP encumbrance: commercial impact high; contribution records, agreements and professional search. Owner: project lead with counsel.

## Market pathway checklist
For a US microwave product, assess radiation-emitting product obligations and the microwave standard identified in the official safety source [S1]. Review electrical safety, EMC, food-contact materials, labeling, sanitation, refrigerants and service requirements for the actual configuration. Requirements for a commercial kitchen unit may differ from a household appliance. For other markets, obtain a jurisdiction-specific assessment rather than treating US requirements as universal.

## Food-process boundary
Commercial storage-cooling requirements cited in [S2] are not a universal serving rule. Applicable local adoption and the intended process matter. A serving target selected below hot-holding temperatures is an immediate-service choice, not indefinite holding permission. An appliance cannot reverse toxins, spoilage or earlier temperature abuse simply by reheating or chilling.

## Claims release checklist
For every claim, name the endpoint, load envelope, sample size, comparison method, uncertainty and reviewer. Safety improvement needs appropriate hazard or outcome evidence. Nutrient claims need food-specific analytical studies. Environmental claims need lifecycle boundaries and measured inputs. Regulatory compliance must name the exact product and market, not a future platform family.

## Incident response
Disable and isolate affected equipment, obtain appropriate emergency assistance if needed, preserve logs and hardware, notify the designated responsible person and document facts. Establish reporting duties with counsel for any commercial pilot. No restart after a critical incident without independent technical clearance and an approved correction plan.
''')

add('10_Impact_and_Access','Global access and environmental measurement plan', '''
## Purpose
Translate the platform's public-benefit intent into decisions that can be measured and revised. Benefits across regions and users will vary. Access, affordability and ecological performance must be designed and tested rather than inferred from premium branding.

## Access architecture
Use a shared control core for a premium paired appliance, a simpler beverage dock, a cooling finisher and a community-kitchen version. Maintain the same essential protective controls across tiers. Publish compatible vessel requirements where feasible and avoid mandatory subscriptions for core operation. Provide tactile controls, readable status, selectable units and instructions that do not rely on color or voice alone.

## Affordability hypotheses
Premium sales may help fund shared engineering, but cross-subsidy is not assumed until a viable margin exists. Test repair access, equipment leasing and community ownership against direct sale. Record total cost of ownership, including energy, cleaning, parts and downtime. Low purchase price with expensive proprietary consumables may undermine access.

## Environmental boundaries
Measure wall energy for the whole thermal task, including refrigeration preconditioning, pumps, mixing, standby and thermal-storage charging. Count material production, refrigerant choice and leakage, replacement parts and end-of-life handling in later lifecycle work. Recovered heat counts as beneficial only when it displaces an actual useful heat demand. Do not label stored or recovered energy as free energy.

## Proposed indicators
Technical: endpoint error, spatial variation, failures, energy per defined task and cleaning time. User: task frequency, interventions, accessibility issues and willingness to evaluate. Service: repair turnaround, module replacement rate and spare-part availability. Environmental: whole-cycle energy, measured food discarded in a defined pilot and estimated material footprint with stated assumptions. Access: nonpremium price, compatible-vessel availability and service coverage.

## Community pilot requirements
Co-design with local operators before deployment. Confirm power supply, water, ventilation, cleaning capacity, language and service support. A communal device with higher utilization may improve cost per task but increases hygiene and scheduling demands. Budget training and support rather than exporting an unsupported prototype.

## Ethical boundaries
Do not test on vulnerable users to accelerate commercialization. Avoid medical or therapeutic framing without appropriate evidence. No animal testing is planned for this feasibility program. Protect participant choice and privacy. Make core controls understandable and allow users to decline data export without losing basic appliance functionality.

## Review cadence
Review indicator definitions at each gate. Publish positive and negative results with limitations. Before making any broad health or sustainability claim, identify the additional study needed and its cost. Stop features that consume resources without a demonstrated useful outcome.
''')

add('11_Outreach_and_Application_Copy','Universal outreach drafts and application responses', '''
## Technical reviewer email
Subject: Review request for a precision heating and cooling feasibility study

Hello,

I am developing THERMA COMMONS, a concept-stage platform for heating and actively cooling defined food and beverage loads to a verified temperature target. I am starting with a stirred-liquid demonstrator so that measurement, cleanability and energy use can be tested before pursuing an integrated appliance.

Would your team consider a short technical scoping conversation? I am seeking review of the thermal architecture, independent measurement approach and a proposed 12-week validation plan. I can share a nonconfidential brief first and agree on any paid review scope before work begins.

The first-phase target is +/-1 degree C for specified water loads under a declared test protocol. This is a proposed development target; no prototype performance or food-safety validation is claimed.

Best regards,
Gerard Ando
g.ando@gkitchen.in

## Sponsorship email
Subject: Milestone-based support for a verified temperature-control demonstrator

Hello,

I am seeking a feasibility partner for THERMA COMMONS, a modular heating and cooling concept centered on measured serving-temperature outcomes. The initial project is deliberately narrow: a cleanable stirred-vessel rig, independent reference measurements and a documented validation campaign.

The proposed request is $25,000 across four decision gates over 12 weeks, with an optional separately valued in-kind contribution. Deliverables include the demonstrator, test data, a reviewed report and a clear decision on whether further development is justified.

Would a brief fit discussion be appropriate? The attached executive brief describes the scope and evidence targets. Sponsorship benefits and any IP or evaluation rights would be agreed separately before work begins.

Best regards,
Gerard Ando
g.ando@gkitchen.in

## Component or laboratory partnership email
Subject: Defined equipment or measurement partnership for a thermal-control prototype

Hello,

I am seeking qualified support for a heating and cooling feasibility rig using defined water loads. The immediate needs are a suitable cooling assembly, independent temperature logging, calibration access and engineering review of the wet-zone design.

Could your team advise whether a small scoped equipment loan, test-service engagement or in-kind contribution fits your capabilities? I can provide requirements and an inventory of requested resources. Ownership, permitted use, attribution and return obligations would be documented before transfer.

Best regards,
Gerard Ando
g.ando@gkitchen.in

## Follow-up email
Subject: Follow-up on the temperature-control feasibility brief

Hello,

I am following up on the THERMA COMMONS brief. My immediate request is a fit assessment for the defined liquid demonstrator, especially measurement and thermal integration. If another function handles early technical partnerships, a referral would be helpful. I can send a shorter scope summary if preferred.

Thank you,
Gerard Ando

## Application description
THERMA COMMONS is a concept-stage modular appliance platform combining active heating, cooling and temperature verification. Its first demonstrator uses a removable stirred vessel and independent reference sensors to test repeatable endpoints for defined water loads. Later development may extend to meal trays and paired cooking/chilling chambers. The project seeks evidence for user convenience, thermal accuracy and practical energy use without assuming broad food-safety or health benefits.

## Assistance requested
1. Thermal-controls engineering and independent measurement support for a 12-week feasibility study.
2. Milestone-based prototype funding or clearly valued equipment and laboratory access.

## Short project summary
Develop and test a precision heating and cooling demonstrator that verifies temperature outcomes for defined loads, establishing a credible foundation for a modular appliance family.

## Keywords
precision temperature control, active cooling, controlled heating, thermal metrology, cleanable vessel, food appliance research, accessible design, repairability, refrigeration, prototype validation

## Submission safeguards
These are drafts for review and adaptation. No messages have been sent. Replace the generic greeting only after verifying recipient identity and role. Confirm attachment version, applicant eligibility and requested amount before each submission. Do not add unverified affiliations, credentials or commitments.
''')

add('12_Pitch_Narrative_and_FAQ','Pitch narrative and diligence questions', '''
## Ten slide speaking outline
1. User problem: show one real workflow in which heating time does not deliver a predictable serving result. Use a documented observation when available.
2. Product proposition: selected temperature plus measured confidence, with active heating and cooling.
3. First demonstrator: a cleanable stirred vessel with independent references; show a diagram rather than a fictional finished product.
4. Architecture: thermal dock, load interface, sensing, controller and offline status.
5. Existing alternatives: heating appliances, probe-controlled systems and domestic chilling already exist; define the narrower workflow opportunity.
6. Evidence plan: 60 final water trials, frozen acceptance rules, uncertainty and comparator data.
7. Product path: dock, defined trays, paired appliance; research options remain gated.
8. Partnership model: paid review, feasibility sponsorship, co-development and later licensing.
9. Budget and team: $25,000 cash, optional $10,000 in-kind; founder identified and specialist roles open.
10. Ask: approve scoping, designate technical counterparts and release Gate A after contracting.

## Sixty second pitch
People often choose a heating time when what they really want is a reliable temperature. THERMA COMMONS is a proposed platform that combines heating, active cooling and measurement to manage that outcome for defined food and beverage loads. We are beginning with a stirred-liquid demonstrator, where repeatable measurement is achievable, before expanding into meal trays or an integrated appliance. We seek $25,000 for a 12-week, stage-gated feasibility study, plus optional laboratory or equipment support. The result will be a demonstrator, independently reviewed data and an honest decision about the next stage.

## Diligence answers
Is it built? No. This package proposes concept-stage feasibility work.
Is it a microwave that cools? The broader appliance may combine RF heating with a separate refrigeration subsystem. Microwave energy itself does not provide the cooling mechanism.
How exact is exact? The initial target is +/-1 degree C for specified mixed water loads, accounting for measurement uncertainty. It is not a promise for every point in arbitrary foods.
What is new? Potentially the implementation and verified workflow. Broad novelty and patentability are unresolved.
Why not start with solid-state RF? It adds cost and specialist complexity before establishing user value and measurement performance.
What is the largest technical risk? Maintaining useful speed, accuracy and cleanability together within an affordable architecture.
What proves health benefits? Nothing in the initial thermal study. Food-specific and outcome-specific studies would be required.
What does sponsorship buy? Agreed experiments, documentation, demonstrations and reporting; not guaranteed success or automatic IP ownership.
What happens if the target fails? Report results, diagnose the cause and choose a bounded redesign or stop decision before further spending.
Why might licensing be attractive? It can use an established partner's manufacturing and service capacity, with negotiated tradeoffs in control and revenue.
What team exists? Gerard Ando is the project lead. Specialist engineering, metrology and food-science roles remain unconfirmed.
What is the next practical milestone? An independently reviewed architecture, measurement plan and safe bench-test scope.
''')

add('13_Evidence_Register','Evidence register and claims ledger', '''
## Source scope
Primary sources checked November 2, 2026. These support bounded technical context; they do not validate this proposed device. Product pages describe their manufacturers' products and should not be treated as independent comparative tests. Specific sponsor programs, eligibility and current funding calls have not been researched in this universal package.

## S1 Microwave safety and regulation
Official source: Microwave Ovens.
https://www.fda.gov/radiation-emitting-products/resources-you-radiation-emitting-products/microwave-ovens
Supported context: microwave ovens have established safety requirements and manufacturer obligations. This source does not approve the proposed platform. Action: have a qualified reviewer identify obligations for the actual RF configuration before development or marketing claims.

## S2 Commercial food cooling context
Official source: 2022 Food Code, section 3-501.14.
https://www.fda.gov/media/184685/download
Supported context: cooked foods requiring time/temperature control are cooled from 135 to 70 degrees F within two hours, then to 41 degrees F or below within six hours total under the model code. Local adoption and intended use determine applicable requirements. This is a storage-cooling criterion, not a universal immediate-serving rule.

## S3 Existing electromagnetic and conventional cooking
Manufacturer technical assistance: Why am I only allowed to cook at one level in the Dialog oven in the M Chef operating modes.
https://www.miele.co.uk/support/customer-assistance/dialog_oven-1255/all/why_am_i_only_allowed_to_cook_at_one_level_in_the_dialog_oven_in_the_m_chef_operating_modes-143926093451
Supported context: a commercial precedent combines electromagnetic and conventional heating. No inference of clearance, novelty or superiority follows.

## S4 Existing domestic chilling and warming functions
Manufacturer product page: Freddy multifunctional blast chiller.
https://www.irinoxhome.com/en/products/abbattitori/freddy
Supported context: domestic appliances already offer chilling and low-temperature cooking functions. Treat nutrition and preservation statements as manufacturer claims, not evidence for this project.

## Claims ledger
C01 Developing a heating and cooling platform: concept description; permitted with concept-stage qualification.
C02 +/-1 degree C: proposed target only; release as a measured claim only after the defined validation and uncertainty review.
C03 Safer than alternatives: unproven; requires a relevant comparative hazard or outcome study.
C04 Healthier or preserves nutrients: unproven; requires food-specific analytical evidence and careful wording.
C05 Lower energy: unproven; requires whole-cycle comparator measurement with equivalent endpoints.
C06 Novel or patentable: unresolved; requires professional prior-art and patent analysis.
C07 Affordable worldwide: aspiration; requires regional cost, service and user evidence.
C08 Heat recovery saves energy: conditional; requires measured useful heat displacement and system accounting.
C09 Sponsor-ready: package prepared for discussion; applicant eligibility and program-specific documentation remain to be completed.

## Engineering calculation
For 0.5 kg of water-like material, assumed specific heat 4 kJ per kg per degree C and a 40 degree C temperature reduction: required heat removal is approximately 80 kJ. At a constant 200 W net heat extraction from the load, idealized time is 400 seconds, approximately 6.7 minutes. This is an arithmetic estimate, not measured device performance. Vessel mass, changing heat transfer, ambient gains and refrigeration input change real results.

## Evidence to obtain next
Traceable temperature measurements; actual engineering and component quotations; documented customer workflows; cleanability review; regulatory classification advice; prior-art and freedom-to-operate assessment; independent evaluation of the final dataset. Update this register whenever public claims change.
''')

add('14_Execution_and_Data_Room','Execution checklist and diligence data room', '''
## First ten working days
Day 1: Confirm project identity, contact details, applicant entity and available budget. Select the liquid demonstrator as the only initial build scope.
Day 2: Recruit a qualified thermal-controls reviewer and an independent measurement reviewer. Confirm rates and availability.
Day 3: Freeze the use case, initial exclusions, vessel geometry and measurement locations.
Day 4: Review architecture, wet-zone hazards, refrigeration selection and safe test-site requirements.
Day 5: Obtain at least two relevant quotations or explain sole-source choices. Update the budget.
Day 6: Finalize the uncertainty budget and proposed validation matrix.
Day 7: Agree on background IP, deliverables, data access and publication terms before detailed technical disclosure.
Day 8: Prepare recipient-specific brief and support request; verify eligibility and authorized contact.
Day 9: Request a fit meeting or paid scoping review using the approved nonconfidential materials.
Day 10: Record feedback, resolve scope changes and submit only the applicable documents. Record submissions and commitments.

## Data room folders
01 Corporate: entity status, signatory authority, contact and required registrations.
02 Technical: requirements, architecture, drawings, component ratings and revision history.
03 Evidence: calibration, raw data, analysis, deviations, comparator results and reviewer report.
04 Finance: cost assumptions, quotations, cash ledger, in-kind ledger and gate reports.
05 IP: contributions, agreements, disclosure log, searches and professional opinions.
06 Safety: hazard register, incident log, training and market-specific compliance plan.
07 Commercial: interview records, pilot agreements, customer permissions and pricing research.
08 Partnership: correspondence, sponsor statements of work, benefits and reporting obligations.

## Recipient-specific submission checklist
Verify organization and recipient; confirm the current opportunity and deadline; map criteria to evidence; confirm applicant eligibility; tailor the request; remove irrelevant annexes; complete mandatory declarations; obtain signatory review; retain the exact submitted version and confirmation. Do not send this entire data room indiscriminately.

## Materials that cannot truthfully be finalized yet
Completed grant applications require a selected program. A supplier-qualified BOM needs architecture review and quotes. Patent documents require actual inventor contributions and counsel. Certification submissions need a defined design and laboratory results. Financial statements require actual records. Letters of support, team biographies and institutional commitments require the contributors' approval. Executed contracts, insurance evidence and banking information must come from the real parties. This package supplies the preparation structure, not fabricated substitutes.

## Weekly project report template
Reporting period; completed work; spend and commitments; updated risks; test outcomes; deviations; decisions required; next gate; owner and due date. Include negative findings and whether they change the investment case.

## Decision record template
Decision identifier; date; question; alternatives considered; evidence; cost and risk effects; selected action; approvers; conditions for reversal; review date.

## Fastest credible route
Secure a bounded technical review, obtain a safe hosted bench environment, use off-the-shelf qualified modules and predefine evidence. Seek a paid pilot or co-development contract only once the first measurements justify it. Keep broad research branches available without making them prerequisites for the first useful result.
''')

budget={'currency':'USD','status':'planning assumptions not quotations','cash_items':[{'item':n,'amount':v} for n,v in [('Thermal hardware and fabrication',4000),('Sensors logging calibration',2500),('Controls protection enclosure',2000),('Specialist engineering',6000),('Independent testing review',2500),('Consumables cleaning',1000),('Discovery accessibility',1000),('Coordination documentation',2000),('Contingency',4000)]],'cash_total':25000,'optional_in_kind_total':10000,'gate_releases':[5000,8000,8000,4000]}
assert sum(x['amount'] for x in budget['cash_items'])==budget['cash_total']==sum(budget['gate_releases'])
(ROOT/'Budget_Model.json').write_text(json.dumps(budget,indent=2))
(ROOT/'Test_Log_Template.json').write_text(json.dumps({'protocol_version':'1.0','trial_id':None,'randomization_seed':None,'device_revision':None,'firmware_hash':None,'operator':None,'mass_g':None,'ambient_C':None,'start_C':None,'target_C':None,'reference_sensor_ids':[],'reference_uncertainty_C':None,'samples':[{'timestamp':None,'control_C':None,'reference_C':[None,None,None],'wall_energy_Wh':None,'state':None}],'completion_time_seconds':None,'spatial_range_C':None,'guard_banded_error_C':None,'pass':None,'deviation':None},indent=2))

styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyCustom',fontName='Helvetica',fontSize=10,leading=14,spaceAfter=8,textColor=colors.HexColor('#223344')))
styles.add(ParagraphStyle(name='HeadCustom',fontName='Helvetica-Bold',fontSize=13,leading=17,spaceBefore=12,spaceAfter=7,keepWithNext=True,textColor=colors.HexColor('#11666b')))
styles.add(ParagraphStyle(name='TitleCustom',fontName='Helvetica-Bold',fontSize=25,leading=29,spaceAfter=18,textColor=colors.HexColor('#102c3b')))
def page(c,d):
    c.setStrokeColor(colors.HexColor('#c9d9dc'));c.line(48,42,564,42)
    c.setFont('Helvetica',8);c.setFillColor(colors.HexColor('#516470'))
    c.drawString(48,29,'THERMA COMMONS  |  Concept-stage feasibility proposal  |  02 Nov 2026')
    c.drawRightString(564,29,str(d.page))
def render(path, chosen):
    story=[]
    for idx,(_,title,txt) in enumerate(chosen):
        if idx:story.append(PageBreak())
        for block in txt.strip().split('\n\n'):
            if block.startswith('# '):
                story.append(Paragraph(html.escape(block[2:]),styles['TitleCustom']))
            elif block.startswith('## '):
                head, _, rest = block.partition('\n')
                story.append(Paragraph(html.escape(head[3:]),styles['HeadCustom']))
                if rest: story.append(Paragraph(html.escape(rest).replace('\n','<br/>'),styles['BodyCustom']))
            else:
                story.append(Paragraph(html.escape(block).replace('\n','<br/>'),styles['BodyCustom']))
    SimpleDocTemplate(str(path),pagesize=(612,792),rightMargin=48,leftMargin=48,topMargin=48,bottomMargin=56,title='THERMA COMMONS '+path.stem,author='Gerard Ando').build(story,onFirstPage=page,onLaterPages=page)
render(ROOT/'THERMA_COMMONS_Complete_Proposal.pdf',docs)
render(ROOT/'THERMA_COMMONS_Executive_Brief.pdf',[docs[1]])
for f in ROOT.glob('*.pdf'):
    reader=PdfReader(f)
    assert len(reader.pages)>0
    assert all((p.extract_text() or '').strip() for p in reader.pages)
    print(f.name,len(reader.pages),'pages')
(ROOT/'README.md').write_text('# THERMA COMMONS sponsorship package\n\nStart with 00_Start_Here.md. The complete PDF combines all 15 documents. Individual Markdown files are editable source documents. JSON files provide editable budget and test-log structures. All project performance and budgets are proposed, not demonstrated.\n')
with zipfile.ZipFile(ROOT.parent/'THERMA_COMMONS_Sponsorship_Package.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(ROOT.iterdir()):
        if p.is_file() and p.name!='build_package.py': z.write(p,'THERMA_COMMONS/'+p.name)
print('Package complete',len(docs),'documents')
