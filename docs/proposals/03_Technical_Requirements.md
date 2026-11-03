# Technical architecture and preliminary requirements

THERMA COMMONS | November 2, 2026 | Version 1.0

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
