# Security and operational boundaries

This project contains no authentication system, telemetry service or hardware network interface. Keep credentials, instrument access tokens and private pilot data out of commits. Do not load untrusted plugins or execute code embedded in measurement records; the current parser reads JSON values only.

For a security concern, contact g.ando@gkitchen.in with a minimal description and affected version. Avoid posting credentials or private participant data in public issues. No response-time guarantee is offered.

Software tests are not physical safety assurance. The reference state machine is for research and cannot provide electrical isolation, refrigerant safety, validated food processes or regulatory conformity.
