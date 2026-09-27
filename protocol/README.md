G7Forge Protocol

The protocol layer is responsible for communicating with the GameSir G7 Pro and interpreting the data exchanged with the controller.

The protocol layer should describe what the controller is being asked to do without depending on a specific connection method.

Responsibilities

The protocol layer will eventually handle:

* Controller identification
* Handshake
* Packet construction
* Packet parsing
* Register reads
* Register writes
* Profile data
* Button and paddle remapping
* Turbo configuration
* Stick configuration
* Trigger configuration
* MNK configuration
* Read-back verification

Transport Independence

The protocol should not directly depend on USB, Bluetooth, or iOS-specific APIs.

The protocol should communicate through a transport abstraction.

G7Protocol
     │
     │ protocol data
     ▼
Transport
     │
     ├── USB
     ├── Bluetooth
     └── Mock

The protocol determines the meaning of the data.

The transport determines how the data reaches the controller.

Known G7 Pro Research

Current reverse-engineering research has identified the following information for supported G7 Pro configuration interfaces:

Vendor ID:       0x3537
Wired PID:       0x109B
Dongle PID:      0x109C
Amazon Wired:    0x10BA
HID PID:         0x100A
Native PID:      0x1022
Interface:       0
OUT endpoint:    0x02
IN endpoint:     0x82
Report size:     64 bytes

These values come from existing reverse-engineering research and should be verified against the target hardware during development.

Protocol Structure

Current research indicates that G7 Pro configuration uses structured reports and register-style reads and writes.

The implementation should eventually document:

* Report format
* Command markers
* Register addresses
* Read operations
* Write operations
* Response format
* Handshake sequence
* Profile storage format
* Verification process

Profile Configuration

The controller appears to contain persistent profile data.

The project will investigate:

* Profile selection
* Profile reading
* Profile writing
* Profile size
* Profile storage
* Read-back verification
* Which settings persist after disconnecting the application

The desired configuration workflow is:

Read
 ↓
Modify
 ↓
Write
 ↓
Read back
 ↓
Compare
 ↓
Confirm

G7Forge should avoid assuming that a successful write means the controller accepted the configuration.

Whenever possible, writes should be verified by reading the relevant data back from the controller.

Turbo

Turbo is a dedicated feature of G7Forge.

The project will investigate whether Turbo can be configured as persistent controller functionality.

The investigation will distinguish between:

1. Native firmware Turbo
2. Persistent onboard Turbo-related configuration
3. Persistent Turbo behavior implemented through the controller’s supported input functionality
4. Runtime software Turbo

The preferred implementation is persistent controller-side functionality when the hardware supports it.

G7Forge should not require the application to remain open merely to maintain a persistent Turbo configuration if the controller itself can store and execute the behavior.

MNK Mode

MNK functionality is a major research target.

The G7 Pro already provides GameSir software functionality for mouse-and-keyboard configuration. G7Forge therefore needs to determine how that functionality is represented at the protocol and HID levels.

The project will investigate whether the controller can operate in a mode where it exposes keyboard and mouse functionality rather than presenting all input exclusively as a gamepad.

Desired MNK Capabilities

The eventual MNK configuration system should investigate support for:

* Keyboard key bindings
* Mouse button bindings
* Mouse movement
* Mouse sensitivity
* Independent X/Y sensitivity
* Deadzone
* Response curves
* Smoothing
* Stick-to-MNK translation
* WASD movement
* Controller button-to-keyboard mappings
* Controller button-to-mouse mappings
* Output device mode

Important Distinction

The project must distinguish between:

MNK → Controller translation

and:

MNK HID output

The first makes keyboard and mouse input behave like a controller.

The second allows the device to present keyboard and mouse input to the operating system/game.

G7Forge will investigate which behavior the G7 Pro firmware actually supports.

The project should not assume that a feature available in GameSir software is necessarily implemented entirely in the controller firmware.

HID Investigation

The following identifiers require investigation:

PID_HID    = 0x100A
PID_NATIVE = 0x1022

Their relationship to:

* Standard controller mode
* HID mode
* MNK mode
* Native mode
* USB interfaces
* Bluetooth operation

must be determined from the existing implementation and hardware testing.

These identifiers should not be assigned a meaning solely from their names.

Research Rules

G7Forge should distinguish between three categories of information:

Confirmed

Behavior verified through:

* Hardware testing
* Read-back verification
* Protocol captures
* Reliable documentation
* Reproducible experiments

Referenced

Behavior found in existing reverse-engineering projects or documentation but not yet independently verified by G7Forge.

Unknown

Behavior that has not yet been established.

Unknown behavior should be investigated rather than assumed.

Future Protocol Files

The exact file structure may change as the protocol becomes better understood.

Potential components include:

g7_protocol.py
packet.py
registers.py
profile.py
remap.py
turbo.py
mnk.py
hid.py

The architecture should remain flexible enough to accommodate discoveries made during reverse engineering.