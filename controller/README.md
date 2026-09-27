Controller Layer

The controller layer represents the configuration and behavior of the GameSir G7 Pro.

It sits between the application interface and the low-level G7 Pro protocol.

Controller Configuration

The controller layer will eventually represent:

* Profiles
* Button remapping
* Paddle configuration
* Turbo
* Stick configuration
* Trigger configuration
* MNK configuration

Profiles

A profile represents a complete configuration that can be stored and recalled.

A profile may contain:

Button mappings
Paddle mappings
Turbo settings
Stick settings
Trigger settings
MNK settings

The exact contents depend on what the G7 Pro hardware and protocol support.

Turbo

Turbo is a dedicated feature of G7Forge.

G7Forge is not intended to become a general-purpose macro recorder.

The project will investigate:

* Turbo activation
* Turbo levels
* Turbo timing
* Hold/release behavior
* Toggle behavior
* Persistent storage
* Controller-side execution

The preferred behavior is controller-side persistence when supported.

MNK Configuration

MNK configuration is treated as a separate operating mode.

The project will investigate:

* Keyboard mappings
* Mouse mappings
* WASD movement
* Mouse sensitivity
* X/Y sensitivity
* Deadzone
* Response curves
* Smoothing
* Mouse-to-stick behavior
* Keyboard-to-stick behavior
* Keyboard/mouse output mode

Controller Mode

Normal controller mode should preserve standard gamepad behavior.

G7Forge
   ↓
G7 Pro
   ↓
Gamepad input

MNK Mode

MNK mode should investigate whether the G7 Pro can present keyboard and mouse behavior rather than simply translating MNK input into gamepad input.

G7Forge
   ↓
MNK configuration
   ↓
Keyboard / Mouse HID behavior
   ↓
Operating System / Game

The exact implementation must be determined through protocol and hardware research.

Persistence

Where supported, configuration should be stored on the controller so G7Forge does not need to remain running.

Configure
   ↓
Write
   ↓
Verify
   ↓
Disconnect
   ↓
Controller retains configuration