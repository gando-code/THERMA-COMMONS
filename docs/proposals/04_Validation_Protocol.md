# Measurement validation and experimental protocol

THERMA COMMONS | November 2, 2026 | Version 1.0

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
