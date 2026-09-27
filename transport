Transport Layer

The transport layer controls how G7Forge communicates with the GameSir G7 Pro.

The transport layer is intentionally separated from the G7 Pro protocol so that the same protocol implementation can potentially communicate through different connection methods.

Transport Types

G7Forge is planned to support three transport concepts:

USB

USB is the primary transport for initial protocol research and controller configuration.

G7Protocol
    ↓
USBTransport
    ↓
GameSir G7 Pro

Bluetooth

Bluetooth will be investigated as a separate transport.

The goal is to preserve the controller’s normal Bluetooth gamepad functionality while determining whether configuration or other supported operations can be performed through Bluetooth.

G7Protocol
    ↓
BluetoothTransport
    ↓
GameSir G7 Pro

Mock

MockTransport simulates a controller connection without requiring physical hardware.

G7Protocol
    ↓
MockTransport
    ↓
Simulated G7 Pro

MockTransport will allow protocol development and automated testing without constantly connecting the physical controller.

Design Principle

Transport handles data movement.

Protocol handles data meaning.

The transport layer should not decide what a packet means or how a controller profile is structured.

Planned Transport Interface

Each transport should eventually provide common operations such as:

* connect
* disconnect
* read
* write
* connection status

The exact interface will be determined during implementation.

Important Constraint

G7Forge should not require a transport implementation to remain active simply because the controller has already received a persistent configuration.

The desired workflow is:

Connect
   ↓
Configure
   ↓
Write
   ↓
Verify
   ↓
Disconnect
   ↓
Controller continues operating normally