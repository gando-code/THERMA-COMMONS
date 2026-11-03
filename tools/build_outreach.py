from pathlib import Path
import json, html, zipfile
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Table,TableStyle
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from pypdf import PdfReader

root=Path(__file__).resolve().parents[1]; out=root/'docs/outreach'; drafts=out/'drafts'
out.mkdir(parents=True,exist_ok=True); drafts.mkdir(parents=True,exist_ok=True)
(root/'artifacts/outreach').mkdir(parents=True,exist_ok=True)
contacts=[]
def contact(id,org,person,route,phone,url,fit,cost,timing,subject,body,attachments,gate):
 contacts.append(dict(id=id,organization=org,recipient=person,route=route,phone=phone,source_url=url,fit=fit,cost_status=cost,timing=timing,subject=subject,body=body,attachments=attachments,gate=gate,verified_date='2026-11-02',status='not contacted'))

contact('01','LA Regional SBDC','Manufacturing advising team','https://go.smallbizla.org/manufacturing-contact-me','866-588-7232','https://smallbizla.org/resources/manufacturing/',
'Best first no-cost business routing and manufacturing-resource connection. Not an engineering lab or grant maker.',
'No-cost advising is published; engineering work and funding are not promised.','First wave',
'Request for manufacturing advising and prototype-resource referrals',
'''Hello SBDC Manufacturing Team,

I am Gerard Ando, an entrepreneur in Los Angeles County developing THERMA COMMONS, a concept-stage precision heating and cooling platform. The first step is a supervised water-only demonstrator, not an integrated consumer appliance.

I would like no-cost advising on two specific needs: identifying a qualified thermal-controls reviewer and finding an appropriate hosted bench environment or manufacturing-resource referral. We have a proposed $25,000, 12-week feasibility plan, but the budget is not secured or supplier-quoted. I want to confirm the smallest credible scope before approaching funding partners.

Would you connect me with the advisor best suited to an early hardware project and explain any intake or eligibility requirements? I can provide a short brief, preliminary requirements and the public research repository. I would also appreciate guidance on whether current manufacturing technical-assistance programs accept concept-stage applicants.

Thank you,
Gerard Ando
g.ando@gkitchen.in''',
'Executive brief only if requested; paste this text into manufacturing intake.','No-cost intake and one relevant advisor/referral accepted.')

contact('02','California State University Northridge','Dr. Shadi Mahjoob, Thermofluid Research and Design Lab','shadi.mahjoob@csun.edu','818-677-7558','https://www.csun.edu/~smahjoob/',
'Best nearby academic thermal-fit inquiry: experimental thermalfluids and heat-management research. External access and interest unconfirmed.',
'No published project fee or free consultation commitment found. Ask for scope and institutional route.','First wave',
'Bounded thermal review request for a water-only heating and cooling demonstrator',
'''Dear Dr. Mahjoob,

Your lab's work in experimental thermalfluids and heat-management systems appears closely aligned with a narrow feasibility question I am developing locally.

THERMA COMMONS is currently a concept and research-software package. I would like to test whether a removable stirred vessel, coupled to an existing refrigerated/heating circulator, can reach specified water temperatures with a measured uncertainty budget. The initial envelope is 250, 500 and 750 gram loads with endpoints between 20 and 60 degrees C. No prototype accuracy or food-safety performance is claimed.

Would you consider a 20-minute fit discussion, or refer me to the appropriate colleague? If there is interest, I would welcome a separately scoped paid or institutionally sponsored review covering heat-transfer feasibility, sensor placement, major hazards and the minimum useful experiment. A short written critique would be more valuable initially than a full development engagement.

I am also exploring whether supervised external bench work is possible through an approved university arrangement. I understand laboratory access, student participation, costs and IP terms require institutional approval.

Best regards,
Gerard Ando
g.ando@gkitchen.in''',
'Executive brief; technical requirements; link to public repository. Do not send entire archive.','Written fit response, scope, cost and institutional contracting/access route.')

contact('03','Los Angeles Cleantech Incubator','Advanced Prototyping Center operations team; ask switchboard for Stephanie Olwen or APC coordinator','Call 213-358-6500; request APC operations contact','213-358-6500','https://laincubator.org/apc/',
'Local fabrication and electronics facility to screen for supervised thermal work. Published facilities do not establish permission for this experiment.',
'Current membership, supervision, insurance and bench fees require a quote. Old 2017/2018 rate sheets were rejected.','First wave',
'APC facility-fit inquiry for a supervised water-only thermal demonstrator',
'''Hello APC Operations Team,

I am Gerard Ando, a Los Angeles County entrepreneur assessing whether the APC is suitable for a small thermal-controls experiment. Your published electronics and prototyping facilities look relevant, but I would like to confirm permitted work before applying or bringing equipment.

The proposed study uses a manufacturer-approved refrigerated/heating circulator, a removable stirred vessel and independent temperature logging. Loads are water only, 250 to 750 grams, with endpoints from 20 to 60 degrees C. The initial plan excludes RF/microwave hardware, pressure systems, refrigerant modification, food preparation and unattended testing.

Could you confirm whether this type of externally supplied equipment and supervised liquid/thermal work can be considered? I would appreciate the requirements for risk assessment, training, electrical review, spill containment, supervision, insurance and equipment storage, together with current access fees and scheduling.

If suitable, could we arrange a short technical tour or facility-fit call? I am seeking an approved bench environment, not assuming membership provides engineering supervision or certification.

Best regards,
Gerard Ando
g.ando@gkitchen.in''',
'Use the draft as a call brief, then email only the address APC provides. Attach requirements after routing.','Written permission for exact experiment plus named supervisor, fees and site requirements.')

contact('04','Simplexity Product Development','Tamsen Burlak, Director of Business Development, California, via official inquiry form','https://www.simplexitypd.com/contact/','Use official contact form','https://www.simplexitypd.com/san-diego/',
'Commercial alternative to academic review; published mechanical, control and prototyping capabilities. Remote review can avoid travel.',
'Paid service; minimum engagement, availability and pricing unknown. Proposed cap is our negotiation limit, not their rate.','First-wave fallback or parallel quote',
'Fixed-scope feasibility review before a thermal prototype build',
'''Hello Tamsen,

I am seeking a tightly bounded engineering review for THERMA COMMONS, a concept-stage heating and cooling research project. Your team's mechanical and control-system capabilities appear relevant to the initial risk-reduction step.

The first experiment would couple an existing refrigerated/heating circulator to a removable stirred vessel and independently measure 250 to 750 gram water loads across a 20 to 60 degree C endpoint range. We do not yet have physical validation, and the public Python code is simulation and analysis only.

Could you advise whether your team accepts a small fixed-fee review covering architecture, heat-transfer limits, protective controls, measurement feasibility and an initial quote-ready component list? The desired output is a short written go/no-go assessment and revised bench scope, rather than a complete product design.

My initial planning ceiling for that review is $1,500 to $3,000, subject to a mutually agreed statement of work; please let me know if your minimum engagement differs. If the scope is too small, a referral to a qualified independent reviewer would also be valuable.

Best regards,
Gerard Ando
g.ando@gkitchen.in''',
'Executive brief and requirements; include review scope after fit response.','Fixed price, named reviewer, written deliverables, schedule and IP terms accepted.')

contact('05','JULABO USA','Sales and applications team','sales@julabo.us','610-231-0250 option 4','https://julabo.us/contact-us/',
'Off-the-shelf refrigerated/heating circulator inquiry. CORIO CD-200F/CD-201F are screening candidates only; manufacturer must select exact US configuration.',
'Quote needed; ask purchase, demonstration, loan, rental or authorized refurbished options without assuming availability.','First wave after initial requirements review',
'Application selection request for a small external water-vessel thermal study',
'''Hello JULABO Applications Team,

I am evaluating an off-the-shelf refrigerated/heating circulator for a supervised research demonstrator in Los Angeles. The application is an external removable vessel with mixing and independent temperature probes, initially containing only 250 to 750 grams of water. Selected endpoints span 20 to 60 degrees C; planned transitions include 20 to 60 and 60 to 40 degrees C.

Could you recommend the smallest suitable US electrical configuration and compatible external-loop accessories? CORIO models appear relevant, but I would like your application review rather than assume a particular unit is suitable.

Please identify cooling capacity across the actual operating range, allowable heat load and flow restrictions, permitted fluids, overtemperature and low-fluid protections, external-control capabilities, and available listing or conformity documentation for the exact configuration. Bath stability will not be treated as accuracy inside our vessel.

Please also quote total equipment/accessory cost, lead time and any authorized demonstration, rental, loan or refurbished route. We have a $4,000 planning allocation for thermal hardware and fabrication, not an approved purchase order; please flag if that is unrealistic.

Best regards,
Gerard Ando
g.ando@gkitchen.in''',
'One-page module RFQ and requirements; no confidential implementation details.','Application-approved exact model, accessory list, rating documents, capacity data and written quote.')

contact('06','PolyScience','Sales support and applications team','sales@polyscience.com','847-647-0611 or 800-229-7569','https://www.polyscience.com/support',
'Second-source circulator quote; published refrigerated/heated bath and refurbished inventory routes.',
'Current refurbished stock and price unconfirmed; no free unit or sponsorship commitment.','Second-source quote in first wave',
'Refrigerated/heated circulator selection and refurbished availability inquiry',
'''Hello PolyScience Sales Team,

I am comparing practical laboratory heating/cooling options for THERMA COMMONS, a concept-stage thermal-control study. Your refrigerated/heated circulating baths and published refurbished-inventory route appear relevant to keeping the first experiment small.

We plan a supervised external stirred vessel with 250, 500 and 750 gram water loads, independent reference measurements and endpoint targets from 20 to 60 degrees C. The key task is to heat and actively cool the load reproducibly; we are not selecting equipment based on bath display resolution alone.

Would you recommend an appropriate US-rated model, external-loop accessories and fluid configuration, including cooling performance at our operating temperatures? Please provide protection features, electrical requirements, conformity documents, control/logging options and limitations for the external vessel arrangement.

Could you quote a new unit and any currently available authorized refurbished alternative, including warranty, calibration options and lead time? Our thermal-hardware/fabrication allowance is $4,000 and may need revision after quotations. A short application call would help avoid buying an oversized or unsuitable system.

Best regards,
Gerard Ando
g.ando@gkitchen.in''',
'Module RFQ; exact same load envelope as JULABO for comparable quotations.','Comparable total-cost quote and application suitability response.')

contact('07','Transcat Los Angeles calibration laboratory','Fullerton laboratory calibration services team','https://www.transcat.com/calibration-and-repair-request','714-447-4445; central 800-828-1470','https://www.transcat.com/calibration-lab-los-angeles',
'Local independent calibration inquiry, with published temperature capabilities and accreditation. Verify the exact scope, uncertainty and system service needed.',
'Paid quote; calibration is not a promise to host experiments or validate the whole prototype.','First wave',
'Quote for a three-channel temperature reference chain and uncertainty review',
'''Hello Transcat Fullerton Team,

I am planning a water-only heating/cooling study and need an independent reference measurement chain, separate from the prototype's control sensor.

The proposed setup uses three immersed reference probes between 20 and 60 degrees C. Our development target is +/-1 degree C at the load, with a preferred expanded reference-chain uncertainty no greater than 0.3 degree C where achievable. The complete chain includes probes, excitation, wiring, logger and the acquisition settings used during testing.

Could you quote suitable calibration services and advise whether you can help select or rent an appropriate reference system? We need fresh readings on all three channels at least once per second with timestamps; headline scan rate or logger resolution alone will not establish suitability.

Please identify accredited scope coverage, calibration points, reported uncertainty and coverage factor, as-found/as-left results, turnaround and cost. If protocol review or onsite measurement support is outside your calibration scope, please quote it separately or refer us appropriately. Our initial metrology/calibration allowance is $2,500, so a minimal fit-for-purpose configuration is preferred.

Best regards,
Gerard Ando
g.ando@gkitchen.in''',
'Measurement RFQ; protocol; list of instrument models after selection.','Quoted complete-chain service with scope and uncertainty confirmed, not generic accreditation alone.')

contact('08','Keysight Technologies','New-product sales/application team for DAQ970A/DAQ973A','https://www.keysight.com/us/en/contact.html','800-829-4444','https://www.keysight.com/us/en/contact.5420.html',
'DAQ candidate selection. Published RTD support is relevant; fresh three-channel sampling at required precision needs confirmation.',
'Purchase/rental/refurbished options require quote and vendor routing. Not an approved BOM selection.','If host laboratory cannot supply a suitable reference logger',
'DAQ selection question for three calibrated RTD channels at one fresh reading per second',
'''Hello Keysight Applications Team,

I am selecting an independent measurement system for a small thermal-controls feasibility study. Could you advise whether a DAQ970A/DAQ973A configuration, or a lower-cost appropriate alternative, fits three immersed four-wire RTD channels over 20 to 60 degrees C?

We require at least one fresh reading per second on every active channel, recorded timestamps, controlled channel-to-channel skew and a defensible combined probe/logger uncertainty. A preferred expanded reference-chain uncertainty is no greater than 0.3 degree C, subject to calibration and review. We do not want to infer performance from a maximum scan-speed specification that uses different settings.

Please recommend the exact mainframe, switching module, RTD wiring, integration/autozero settings and software/export arrangement, with the resulting three-channel scan timing and temperature accuracy. Please identify an authorized calibration and rental or refurbished route if available; borrowing suitable equipment from the host lab is our first preference.

The project is concept-stage and water-only. I can provide the proposed protocol for an application-fit discussion before any order.

Best regards,
Gerard Ando
g.ando@gkitchen.in''',
'Measurement RFQ; use new-product contact form, not the published order mailbox.','Written configuration and actual configured scan/uncertainty assessment.')

contact('09','Intertek','Appliances and Consumer Electronics Safety Testing team','https://www.intertek.com/appliances/safety-testing/contact/','800-967-5352','https://www.intertek.com/appliances/safety-testing/contact/',
'Early classification and precompliance consultation for intended product. A consultation does not authorize bench work or certify a complete appliance.',
'Paid scope likely; ask minimum fixed-fee desk review. No fee published in reviewed page.','After reviewer has one-page architecture; before custom powered build',
'Pre-design classification review for a combined heating and cooling appliance concept',
'''Hello Intertek Appliances Team,

I am seeking a bounded pre-design consultation for THERMA COMMONS, a concept-stage modular heating and cooling appliance. The immediate feasibility rig would use a manufacturer-approved laboratory circulator, a removable stirred vessel and independent reference probes, with water-only supervised testing.

Before custom electrical integration, I would like to identify the likely safety and conformity pathway for a future household or commercial beverage/food-temperature device in the US. These are alternative intended-use paths to assess, not a request to certify an undefined product.

Could you quote a short desk review identifying the likely applicable requirements, critical architecture decisions, food-contact/sanitation considerations and which component evidence would reduce later testing effort? Please distinguish the existing module's certification from assessment of the final assembly.

RF heating, pressure operation and food-process claims are outside the initial rig. Any future RF version would receive a separate review. Please advise the minimum information and fixed-fee scope needed for a useful early opinion.

Best regards,
Gerard Ando
g.ando@gkitchen.in''',
'Architecture, intended-use alternatives, module documents after selection.','Written scope and requirements assessment; no claim of product certification.')

contact('10','Frontier Energy Food Service Technology Center','FSTC equipment-performance and research team; request routing to David Zabrowski team','https://frontierenergy.com/form/footer-contact','510-444-8707','https://frontierenergy.com/food-service-technology-center',
'Best specialist later-stage commercial-foodservice measurement and benchmark discussion; published fuel-neutral lab and equipment research.',
'Research services, host access and any utility eligibility require confirmation. No paid pilot funding inferred.','Protocol-fit inquiry now; commissioned test or pilot only after bench evidence',
'Protocol-fit inquiry for a future foodservice heating and cooling workflow study',
'''Hello FSTC Team,

I am developing THERMA COMMONS, a concept-stage platform for controlled heating and active cooling to selected serving temperatures. Your equipment-performance and foodservice energy-research work appears relevant to defining a credible comparison before we seek a commercial pilot.

We are first planning a water-only stirred-vessel study with independent references. No physical performance, food-safety benefit or energy saving has been established. The immediate question is which measurements would make later hospitality workflow results useful to your team or an equipment partner.

Could we arrange a short fit discussion about whole-cycle energy boundaries, equivalent-load comparisons, operator time and whether a relevant test method exists or a custom protocol would be required? If appropriate, I would appreciate the requirements and budget range for a later scoped laboratory evaluation, after the first measurements justify it.

We would not describe this nonstandard concept as ENERGY STAR eligible or seek a paid customer pilot without evidence and a reviewed operating process. Please route this inquiry to the appropriate equipment-performance or research contact.

Best regards,
Gerard Ando
g.ando@gkitchen.in''',
'Executive brief now; measured results and protocol only after gate passes.','Protocol feedback now; later quote and signed evaluation scope after measured gate.')

contact('11','SoCalGas Food Service Equipment Center','Maria Murillo and Foodservice Team, via published program mailbox','ercfoodsvc@socalgas.com','562-803-7323','https://www.socalgas.com/business/education/food-service-equipment-center/try-before-you-buy',
'Nearby foodservice workflow/referral resource in Downey. Natural-gas equipment focus reduces fit for an electric-only concept.',
'Eligibility, outside-prototype acceptance and any charges unconfirmed. Not a free external engineering lab or paid-pilot commitment.','Discovery/referral only now; equipment evaluation later if explicitly accepted',
'Foodservice workflow and appropriate test-partner referral request',
'''Hello Maria and Foodservice Team,

I am a Los Angeles County entrepreneur researching a proposed precision heating and active-cooling workflow for beverages and defined meals. Your Food Service Equipment Center's operator education and equipment-comparison work may help us identify a useful hospitality problem before building a product.

Our initial feasibility plan is water-only and uses electric laboratory equipment; it does not yet have physical validation. I recognize your center's natural-gas equipment focus and do not want to assume our concept qualifies for your programs or that outside prototypes can be brought onsite.

Could you advise whether a brief workflow discussion or referral is appropriate? I would particularly value guidance on reheating/cooling bottlenecks, operator comparison metrics and a suitable independent electric-appliance or foodservice test resource. If future evaluation could be considered, please explain the eligibility, safety, insurance and equipment-acceptance requirements first.

We are not requesting a rebate, equipment installation or paid pilot at this stage. A short fit conversation or referral would be the most useful next step.

Best regards,
Gerard Ando
g.ando@gkitchen.in''',
'Short brief only if requested; no equipment onsite without written acceptance.','Relevant referral or documented eligibility response; deprioritize if electric-only mismatch.')

contact('12','LACI Startup Programs','Pipeline team','pipeline@laincubator.org','213-358-6500','https://laci.smapply.org/prog/incubation_program/',
'Later cleantech pilot/incubation route if measured impact, prototype, staffing and rights eligibility align. Not a substitute for first experiment.',
'Main program page states 1.5-3 percent equity warrant; confirm current cohort terms. Not free or guaranteed funding.','One fit inquiry now; apply later only if eligible',
'Early fit check for future incubation after thermal feasibility evidence',
'''Hello LACI Pipeline Team,

I am developing THERMA COMMONS in Los Angeles County, beginning with a narrow water-only heating/cooling feasibility study. The longer-term platform may support efficient foodservice workflows, but we have not yet demonstrated energy or waste-reduction benefits and do not have a validated physical prototype.

I noticed that the Cohort 14 application portal lists an opening on December 1, 2026. Before planning an application, could you confirm the current cohort's readiness requirements, program duration, dates and warrant terms? The general program page and cohort portal appear to describe different program structures.

Our public research software is MPL-2.0 licensed; proposal materials and separately developed rights are reserved. We should not assume this satisfies the proprietary-technology eligibility criterion. I would appreciate guidance on what evidence and rights position you would need to see.

For now, is an APC access inquiry or another early-stage pathway more appropriate than incubation? I would prefer a clear readiness milestone over applying prematurely. No financing or pilot commitment is assumed.

Best regards,
Gerard Ando
g.ando@gkitchen.in''',
'Executive brief; later measured evidence. Coordinate with APC request rather than duplicate outreach.','Written fit/readiness guidance and current terms; no application until readiness confirmed.')

plan='''# THERMA COMMONS partner execution research

Research checked November 2, 2026, America/Los_Angeles. Project status: concept-stage. No messages sent, meetings booked, quotations accepted or partnerships established.

## Recommendation

Run a measurement-first, hosted module experiment. Seek one qualified thermal reviewer, one approved host and one independent reference-chain provider. Begin with an established refrigerated/heating circulator instead of custom refrigeration and mains switching. Use university, commercial engineering and shared-facility routes as alternatives; do not make any single institution a dependency.

The first useful result is a measured answer about thermal endpoints, vessel coupling, gradients, time and energy for a defined water load. Existing laboratory circulators already control temperature: demonstrating their bath specification is not product differentiation. The experiment must test our removable-vessel workflow, measurement integrity and usability opportunity. A successful water study is not a food-safety validation or a market-ready appliance.

## Priority and smallest asks

First five actions: submit the SBDC manufacturing intake; request Dr. Mahjoob's fit assessment; call APC operations; send a conditional module-selection inquiry to JULABO; request metrology fit from Transcat. Run a PolyScience second-source quote after the load envelope is consistent. Ask Simplexity for a bounded review if the academic route is unavailable or slow. Borrow host instrumentation before buying a DAQ.

The contact register contains 12 routes across 11 organizations or organizational teams, counting APC and LACI Pipeline separately within LACI. Each record identifies verified public routing, limitations and a tailored draft. Contact facts were published on official sources; mailbox deliverability and willingness to participate have not been tested. No personal email format was guessed. Where no suitable direct mailbox was verified, use the official form or phone route.

## Delivery alternatives

Path A: academic review plus approved hosted bench. Potential advantage: strong measurement expertise and existing equipment. Constraints: faculty interest, institutional contracting, access and IP review; no free access assumed. CSUN is the strongest nearby technical-fit inquiry found, not a confirmed partner.

Path B: commercial fixed-scope review plus approved lab. Potential advantage: defined accountability and a short deliverable. Constraints: minimum engagement and hourly economics may exceed our allowance. Simplexity is a scoped-quote option, not a promise to work within $3,000.

Path C: qualified reviewer plus APC facility, if approved. Potential advantage: local fabrication/electronics infrastructure. Constraints: membership is not supervision or permission for liquid/thermal work. Obtain written acceptance for the exact experiment, a named supervisor and current charges before buying membership.

Path D: supplier-hosted or borrowed-equipment demonstration. Potential advantage: less capital and no early custom cooling subsystem. Constraints: availability, external-vessel acceptance and independent instrumentation; a supplier demo alone is not independent validation.

## Budget and calendar discipline

Keep the current $25,000 feasibility proposal as an unfunded planning envelope. Authorize no spending from this document. The $5,000 first gate covers scoping and preparation; a proposed $1,500-$3,000 review cap is our negotiation ceiling, not a market quote. The $4,000 thermal-hardware/fabrication and $2,500 metrology allowances may be too low for new premium instruments. Compare borrowing, rental, authorized refurbished and purchase using delivered total cost, service and warranty. Do not spend contingency before receiving comparable quotations.

Days 1-3: send five targeted fit inquiries. Days 4-7: compare responses, schedule qualified discussions and ask written scope questions. Day 8: select a provisional reviewer and host, subject to terms. Days 9-10: approve the bounded review and quote-ready requirements. These are our target actions, not supplier response promises. If no reply, follow up once after five business days, then switch to the documented alternative. Do not postpone all work while awaiting a professor or accelerator.

## Bounded review statement of work

Objective: determine whether an existing circulator and removable stirred vessel can test the specified temperature outcomes safely and meaningfully. Inputs: concept brief, technical requirements, proposed 60-trial matrix and public source-code status. Requested outputs: architecture critique; mass/heat-transfer estimate; actual operating envelope; hazard list and independent protections; sensor/scan/uncertainty plan; quote-ready component classes; host requirements; and a written proceed/redesign/stop recommendation. Require a named reviewer and an agreed fixed price before work. Do not expect a final product design or certification in this review.

## Off-the-shelf module qualification

Screen JULABO CORIO refrigerated/heating models and PolyScience refrigerated/heated circulators. A heating-only bath is not equivalent: cooling near or below ambient needs the suitable refrigerated configuration or an approved accessory. The exact voltage variant, protections, permitted fluid, external load, tubing and pressure limitations must be confirmed by the manufacturer. Published stability in a bath is not absolute temperature accuracy or uniformity in our external vessel. Obtain rating documents for the actual configuration; do not infer an NRTL listing from a generic product family. A component approval does not certify our assembly.

Ask for cooling capacity versus temperature under declared test conditions, working fluid, ambient and mains supply; heating power; external flow/pressure limits; safety shutdown behavior; logging/control interface; warranty; approved accessories; service; delivered price; and lead time. Avoid over-sizing from an arbitrary cooling-watt target. Vessel wall, heat-transfer area, coolant approach and mixing may govern performance more than compressor rating.

## Measurement issue that changes procurement

The protocol and current analyzer require three fresh reference channels at least once per second. The PT-104 manufacturer specifies 720 ms conversion per channel and documents that multiple active channels reduce fresh per-channel update rate. A three-channel unit is therefore not a confirmed fit for the existing acquisition requirement; polling cached readings at 1 Hz does not create independent samples. Do not buy it for this protocol without a validated alternative acquisition design or a prospectively approved protocol revision.

Ask Keysight or the host lab for an exact RTD/logger/module configuration and demonstrated scan timing at the chosen integration, settling and autozero settings. Maximum advertised scan rates under other conditions are insufficient. Temperature-chain calibration must include probe, wiring, excitation, logger and settings; sensor class alone does not establish +/-0.3 degree C expanded uncertainty. Record uncertainty coverage factor, drift and response time. Sequential channels require timestamps and a justified skew limit; interpolation cannot silently manufacture simultaneous truth.

## Evidence freeze and software gap

After tuning on separate data, freeze hardware, firmware, probe locations, protocol and analysis. Use the existing 60-trial matrix: three masses, four transitions, five repeats. Keep a complete 60-second verification window, uncertainty guard-banding and the cell-level rules. The current Python analyzer checks complete single-trial normalized records, not calibration authenticity or full campaign acceptance. It cannot authenticate the word measured, and the example record is fabricated. Do not submit the fixture or simulations as evidence.

Before the final campaign, agree a normalization procedure with per-channel fresh-sample provenance. Add or independently prepare a campaign ledger that counts invalid/missing runs and timeouts as failures under the protocol, checks at least 57 of 60 overall and at least four of five per cell, and reports a confidence interval. A 57-of-60 observed result is preliminary evidence, not proof that the population success probability is 95 percent. Keep raw exports unchanged and preserve all deviations.

## Host acceptance checklist

Get written permission for water loads, temperature envelope and every powered module; name the responsible supervisor; confirm electrical review and approved use; review spill containment, drainage, hose retention, ventilation and emergency isolation; confirm training, insurance, equipment storage, operating hours, incident response and waste handling; separate wet and electrical zones; document cleanup and instrument custody. No food, raw animal products, pressure systems, RF or unattended operation belongs in the initial experiment.

## Pilot and co-development gates

Gate 1: reviewer-approved method, host acceptance and quote-backed budget. Gate 2: supervised commissioning and protective-function evidence. Gate 3: frozen measured campaign, reviewed uncertainty, transparent failures and comparator results. Gate 4: a defined food/process review, cleaning/material assessment and usability evidence before any consumable-food pilot. A water study alone does not permit a foodservice deployment.

After Gate 3, ask FSTC for a scoped measurement/comparator engagement and identify a willing operator through qualified introductions. After Gate 4, offer a fixed-scope paid evaluation to a customer only where there is a real buyer need and agreed protections. A contract in which we pay an engineering firm is not a customer-paid pilot. No researched contact has committed to pay us. A paid pilot is a future negotiated outcome, not a funding source we can presently count on.

## Recommended pilot commercial structure

Propose one workflow, one trained site, two to four weeks and a capped number of cycles. Define approved loads, supervision, sanitation, training, uptime expectations, incidents, data access, deliverables, acceptance and termination. Price from actual installation, service, instrumentation, analysis and insurance costs, with agreed margin and contingency. Use milestone invoicing or a deposit only after a signed agreement. No universal pilot price is defensible before this scope exists.

For co-development, define background IP, new inventions, source code, data, publication review, equipment ownership, responsibility for compliance and commercial option terms. MPL permits use of the covered software without royalties under its conditions; it cannot be presented as exclusive proprietary software. Negotiate services, reserved materials and separately owned future implementations on their actual merits. Avoid broad unpaid exclusivity or guarantees of patents, savings or licensing income.

## Accelerator timing and eligibility

LACI is relevant as a later pathway, not the critical path. Its general startup page lists a working prototype, full-time staffing, proprietary-technology criteria and a 1.5-3 percent equity warrant. Its current Cohort 14 portal lists December 1, 2026 opening and a January 15, 2027 deadline field, while narrative text still says deadline TBD in mid-January. The two pages also describe different program durations. Confirm dates, structure, current eligibility and terms with Pipeline. Do not claim acceptance, zero cost, an open application today or guaranteed pilot funding.

SoCalGas is a lower-priority local discovery/referral contact because its center focuses on natural-gas equipment. Ask honestly whether an electric-only project is relevant. Frontier Energy's fuel-neutral equipment-performance work is the stronger later technical comparison fit. Do not buy equipment or travel to a kitchen based solely on a public demonstration program.

## Beyond the first demonstrator

Keep four separate branches in the roadmap: defined soups and trays after food-process review; paired heating/chilling chambers after system evidence; useful heat recovery after measured simultaneous hot/cold demand; and RF/vacuum/solid-state cooling as separately funded research. Premium finishes and connected features should follow validated workflow demand. Use the same reference-data discipline and essential protections in affordable and premium variants.

## Outreach and follow-up practice

Use one recipient and one narrow request per organization. Do not send the entire proposal archive cold. Start with the relevant brief and offer the technical annex. The drafts are ready to adapt to official forms and use Gerard Ando's verified preferred email. Insert only a real phone number, entity and address if a form requires them. Do not invent company registration, secured funding, partner affiliations or results. Mention the public repository as research, not as a finished product.

Follow up once after five business days: I am following up on the bounded fit request below. If this is outside your scope, could you direct me to the appropriate technical contact? A short suitability answer would help us choose our next step. Thank you, Gerard Ando. After a second nonresponse, pause outreach and use the alternative route. Respect opt-outs.

## Research limits

Sources establish published contact routes and stated capabilities, not availability, price, willingness to host external thermal experiments, funding or contractual suitability. Current quotes, liability, insurance, IP and program eligibility remain to be confirmed. Historical APC membership prices and historical CMTC individual contacts were excluded from recommended direct routing. No claim is made that this is an exhaustive worldwide search or that any draft guarantees a response.
'''
# Correct organizational count: SBDC, CSUN, LACI, Simplexity, JULABO,
# PolyScience, Transcat, Keysight, Intertek, Frontier, SoCalGas = 11.
(out/'EXECUTION_RESEARCH.md').write_text(plan)
(out/'CONTACTS.json').write_text(json.dumps(contacts,indent=2)+'\n')
table=['# Verified contact register','', 'Checked November 2, 2026. Published public routing only; no outreach sent.','', '| ID | Recipient | Exact route | Phone | Timing | Source |','|---|---|---|---|---|---|']
for c in contacts:
 table.append(f"| {c['id']} | {c['organization']} - {c['recipient']} | {c['route']} | {c['phone']} | {c['timing']} | [Official source]({c['source_url']}) |")
 text=f"# {c['organization']} tailored outreach\n\nRecipient: {c['recipient']}\n\nRoute: {c['route']}\n\nPhone: {c['phone']}\n\nVerified public source: {c['source_url']}\n\nBest use: {c['fit']}\n\nCost and availability: {c['cost_status']}\n\nWhen: {c['timing']}\n\nSubject: {c['subject']}\n\n{c['body']}\n\n## Attachments and next gate\n\n{c['attachments']}\n\nNext gate: {c['gate']}\n\nStatus: Draft only. Not sent.\n"
 (drafts/(c['id']+'_'+c['organization'].replace(' ','_').replace('/','_')+'.md')).write_text(text)
(out/'CONTACT_REGISTER.md').write_text('\n'.join(table)+'\n')

rfq='''# Universal module and measurement RFQ

## Thermal module

Application: approved supervised water-only external stirred vessel; 250, 500 and 750 gram loads; targets 20, 40 and 60 degrees C. Transitions: 20 to 40, 20 to 60, 60 to 40 and 40 to 20 degrees C. Ambient baseline 20 +/-2 degrees C. Initial trial timeout 30 minutes. Actual sizing and vessel geometry require reviewer approval.

Quote exact configuration, voltage/plug, manufacturer-approved external-loop accessories, working fluids, cooling-capacity curves with test conditions, useful heating power, flow/pressure limits, wetted materials, protective controls, rating/certification documents, external-control limitations, warranty, service, lead time, shipping and taxes. Separate new, authorized refurbished, rental, loan and demonstration options where actually available. State whether a prototype vessel invalidates any warranty or permitted use.

## Independent measurement

Three independent immersed reference channels plus separate control sensor. Reference range 20 to 60 degrees C. At least one fresh sample per second per channel; provide configured scan time, sensor response, skew and timestamp behavior. Preferred full-chain expanded uncertainty <=0.3 degree C, with coverage factor and calibration evidence. No promise that this uncertainty is attainable within our allowance.

Quote probes, logger, excitation, wiring, calibration, software/export and training as a complete chain. Include accredited scope coverage where requested, calibration points, as-found/as-left data, drift allowance, settings and turnaround. A module's display resolution is not accuracy. Keep manufacturer control output separate from reference truth.

## Commercial response

We request a feasibility quote, not a purchase. Identify assumptions, exclusions, substitutes, minimum engagement, quote expiry and service ownership. Our preliminary allowances are $4,000 thermal hardware/fabrication and $2,500 metrology/calibration, not supplier prices or secured funds. Flag an impossible budget rather than silently removing essential protections or measurements.
'''
(out/'MODULE_AND_METROLOGY_RFQ.md').write_text(rfq)

sources=[
('SBDC manufacturing resources','https://smallbizla.org/resources/manufacturing/'),
('SBDC manufacturing intake','https://go.smallbizla.org/manufacturing-contact-me'),
('CSUN thermal lab and published contact','https://www.csun.edu/~smahjoob/'),
('CSUN institutional thermal laboratory page','https://w2.csun.edu/engineering-computer-science/college/research-centers/research-labs/thermofluid-research-and-design'),
('LACI APC','https://laincubator.org/apc/'),
('LACI current staff','https://laincubator.org/laci-staff/'),
('Simplexity California contact','https://www.simplexitypd.com/san-diego/'),
('Simplexity inquiry form','https://www.simplexitypd.com/contact/'),
('Simplexity mechanical engineering','https://www.simplexitypd.com/mechanical-engineering/'),
('JULABO contacts','https://julabo.us/contact-us/'),
('JULABO CORIO CD-200F screening candidate','https://www.julabo.com/en-us/products/refrigerated-circulators/refrigerated-heating-circulators/corio-cd-200f'),
('PolyScience support contacts','https://www.polyscience.com/support'),
('PolyScience refrigerated/heated baths','https://www.polyscience.com/products/circulating-baths/refrigeratedheated-circulating-baths'),
('PolyScience refurbished inventory route','https://www.polyscience.com/refurbished-inventory'),
('Transcat Fullerton laboratory','https://www.transcat.com/calibration-lab-los-angeles'),
('Transcat quote route','https://www.transcat.com/calibration-and-repair-request'),
('Keysight product inquiry route','https://www.keysight.com/us/en/contact.5420.html'),
('Keysight DAQ970A capabilities','https://www.keysight.com/us/en/product/DAQ970A/data-acquisition-system-usb-lan.html'),
('Pico PT-104 conversion specification','https://www.picotech.com/data-logger/pt-104/pt-104-specifications'),
('Pico manufacturer sampling explanation','https://www.picotech.com/support/topic12567.html'),
('Intertek appliances inquiry','https://www.intertek.com/appliances/safety-testing/contact/'),
('Frontier FSTC','https://frontierenergy.com/food-service-technology-center'),
('Frontier contact form','https://frontierenergy.com/form/footer-contact'),
('SoCalGas equipment center','https://www.socalgas.com/business/education/food-service-equipment-center'),
('SoCalGas team contacts','https://www.socalgas.com/business/education/food-service-equipment-center/try-before-you-buy'),
('LACI general eligibility and warrant terms','https://laincubator.org/startupprograms/'),
('LACI Cohort 14 portal and date fields','https://laci.smapply.org/prog/incubation_program/'),
]
source_md='# Source register\n\nChecked November 2, 2026. Official sources; contact facts are not commitments. Date conflicts and program-fit caveats are explained in EXECUTION_RESEARCH.md.\n\n'+'\n\n'.join(f'{i+1}. {t}\n{u}' for i,(t,u) in enumerate(sources))+'\n'
(out/'SOURCES.md').write_text(source_md)
(out/'README.md').write_text('''# THERMA COMMONS execution and contact package

Start with EXECUTION_RESEARCH.md and CONTACT_REGISTER.md. Twelve tailored drafts are in drafts/. CONTACTS.json contains machine-readable routing and status. MODULE_AND_METROLOGY_RFQ.md is the reusable supplier specification. SOURCES.md records primary references. The PDF combines the research and all contact drafts.

These are named outreach annexes; the universal proposal documents remain sponsor-neutral. Nothing has been sent. Every contact remains unconfirmed as a partner. Read the current cost, eligibility and evidence caveats before outreach. These proposal materials remain reserved under the repository rights notice.
''')

styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Body2',fontName='Helvetica',fontSize=10,leading=14,spaceAfter=8,textColor=colors.HexColor('#243b48'),splitLongWords=True))
styles.add(ParagraphStyle(name='Title2',fontName='Helvetica-Bold',fontSize=23,leading=27,spaceAfter=15,textColor=colors.HexColor('#102c3b')))
styles.add(ParagraphStyle(name='Head2',fontName='Helvetica-Bold',fontSize=12,leading=16,spaceBefore=10,spaceAfter=7,keepWithNext=True,textColor=colors.HexColor('#14666b')))
def paragraph(t,style='Body2'):return Paragraph(html.escape(t).replace('\n','<br/>'),styles[style])
def add_md(story,text):
 for block in text.strip().split('\n\n'):
  head,sep,rest=block.partition('\n')
  if block.startswith('# '):story.append(paragraph(head[2:],'Title2'))
  elif block.startswith('## '):
   story.append(paragraph(head[3:],'Head2'))
   if rest:story.append(paragraph(rest))
  else:story.append(paragraph(block))
def footer(c,d):
 c.setFont('Helvetica',8);c.setFillColor(colors.HexColor('#536873'))
 c.drawString(44,28,'THERMA COMMONS | Verified contact research | 02 Nov 2026 | Drafts not sent')
 c.drawRightString(568,28,str(d.page))
story=[];add_md(story,plan)
story.append(PageBreak());add_md(story,rfq)
for c in contacts:
 story.append(PageBreak())
 story.append(paragraph(c['id']+' '+c['organization'],'Title2'))
 for label,key in [('Recipient','recipient'),('Route','route'),('Phone','phone'),('Fit','fit'),('Cost and availability','cost_status'),('Timing','timing'),('Source','source_url')]:
  story.append(paragraph(label+': '+c[key]))
 story.append(paragraph('Subject: '+c['subject'],'Head2'))
 add_md(story,c['body'])
 story.append(paragraph('Attachments: '+c['attachments']))
 story.append(paragraph('Decision gate: '+c['gate']))
story.append(PageBreak());add_md(story,source_md)
pdf=root/'artifacts/outreach/THERMA_COMMONS_Contacts_and_Execution.pdf'
SimpleDocTemplate(str(pdf),pagesize=(612,792),leftMargin=44,rightMargin=44,topMargin=42,bottomMargin=50,title='THERMA COMMONS contact and execution research',author='Gerard Ando').build(story,onFirstPage=footer,onLaterPages=footer)
reader=PdfReader(pdf);assert all(p.extract_text().strip() for p in reader.pages)
with zipfile.ZipFile(root/'artifacts/outreach/THERMA_COMMONS_Outreach_Package.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(out.rglob('*')):
  if p.is_file():z.write(p,p.relative_to(root))
 z.write(pdf,pdf.name)
print('Created',len(contacts),'contact drafts;',len(reader.pages),'PDF pages')
