Application Layer

The application layer will provide the user interface for G7Forge.

The initial application target is iOS.

Planned Interface

The application should eventually provide:

* Controller connection
* Connection status
* Profile selection
* Profile management
* Button remapping
* Paddle configuration
* Turbo configuration
* MNK configuration
* Mouse sensitivity
* Stick response settings
* Deadzone settings
* Read/write controls
* Read-back verification
* Technical controller information

User Experience

The application should make advanced controller configuration understandable without hiding important technical behavior.

Users should be able to see whether a setting has:

* Been changed locally
* Been written to the controller
* Been verified
* Failed to write
* Been read from the controller

Architecture

The UI should not directly construct low-level G7 Pro packets.

The intended flow is:

UI
 ↓
Controller API
 ↓
G7 Protocol
 ↓
Transport
 ↓
G7 Pro

This keeps the UI independent from the underlying communication method.

Future UI Areas

Potential screens include:

Dashboard
Profiles
Remapping
Turbo
MNK
Sensitivity
Controller Information
Advanced / Diagnostics

The final interface will be determined during development.