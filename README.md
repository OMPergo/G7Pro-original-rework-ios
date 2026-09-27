# G7Pro-original-rework-ios
Independent configuration and profile management tool for the GameSir G7 Pro.
G7Forge

An independent configuration and profile-management project for the GameSir G7 Pro controller.

G7Forge is being developed as a learning-driven engineering project. The goal is to understand the controller’s communication protocol, configuration storage, remapping system, macros, Turbo behavior, and connection methods rather than simply relying on proprietary configuration software.

Project Goals

G7Forge aims to eventually provide:

* Controller profile management
* Button remapping
* Paddle/button configuration
* Stick and trigger configuration
* Turbo configuration
* Persistent onboard settings where supported by the controller
* USB configuration support
* Investigation of Bluetooth configuration support
* A user-friendly iOS interface
* Verification that written settings can be read back from the controller
* Mnk key binds and mouse sensitivity on controller

Important Design Principle

G7Forge separates the controller protocol from the connection method.

The protocol layer should understand what the controller is being asked to do.

The transport layer should understand how data is sent to and received from the controller.

This allows the same protocol implementation to eventually work with different transport mechanisms.

                 G7Forge
                    │
                    ▼
             ┌──────────────┐
             │   iOS UI     │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │ G7 Controller│
             │     API      │
             └──────┬───────┘
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
   ┌─────────────┐     ┌─────────────┐
   │ G7 Protocol │     │   Profiles  │
   └──────┬──────┘     └─────────────┘
          │
          ▼
   ┌─────────────────────────┐
   │       Transport         │
   ├───────────┬─────────────┤
   │    USB    │  Bluetooth  │
   └───────────┴─────────────┘

Turbo

Turbo is an explicit research target for this project.

The project will distinguish between:

1. Native controller Turbo functionality, if supported by the G7 Pro firmware.
2. Persistent macro-based behavior, if supported.
3. Software-only Turbo, if the controller cannot store the desired behavior onboard.

The goal is to determine what the original G7 Pro hardware actually supports rather than assuming behavior from other GameSir models.

Development Philosophy

Important protocol decisions, architecture decisions, and controller behavior should be understood and documented by the developer.

Whenever possible, implementations should be:

* Explained before being generated
* Tested independently
* Read back and verified
* Documented with their technical reasoning

Project Status

Early development.

Current focus:

* Establish project architecture
* Understand the existing reverse-engineered G7 Pro protocol
* Build the protocol abstraction
* Build a mock transport for development and testing
* Investigate persistent profile, macro, and Turbo behavior
* Eventually build the iOS interface

Reference

The project uses publicly available reverse-engineering research and existing open-source implementations as technical references.

G7Forge is an independent implementation and is not affiliated with GameSir.
MNK Translation

G7Forge aims to provide a dedicated mouse-and-keyboard-to-controller translation system.

The goal is not simply to remap keyboard buttons to controller buttons. The system should translate keyboard and mouse input into controller-style output in a way that allows the controller to be used as an intermediary between MNK input and games that normally expect controller input.

Keyboard → Controller

The system should support configurable keyboard-to-controller translation, including:

* WASD → left analog stick
* Keyboard buttons → controller buttons
* Modifier keys → controller buttons
* Configurable keybinds
* Configurable analog movement behavior
* Deadzone configuration
* Response curves
* Maximum stick output
* Movement response/acceleration where technically possible

Mouse → Controller

The system should support dedicated mouse-to-right-stick translation.

Mouse movement should be converted into controller right-stick output rather than simply assigning mouse buttons to controller buttons.

The system should eventually support:

* Mouse X → right-stick X
* Mouse Y → right-stick Y
* Horizontal sensitivity
* Vertical sensitivity
* Independent X/Y sensitivity
* Deadzone behavior
* Response curves
* Smoothing where appropriate
* Maximum stick output
* Configurable response behavior
* Separate sensitivity profiles where technically possible

Controller Output

The goal is for the resulting output to behave as a normal controller input to the game.

The translation system should avoid unnecessary software layers between the input device, G7Forge, and the resulting controller output.

The desired architecture is:

Keyboard + Mouse
        ↓
   G7Forge MNK
   Translation
        ↓
 Controller Output
        ↓
      Game

rather than relying on multiple independent input-mapping systems simultaneously.

Research Requirement

MNK translation is a major engineering feature and should not be assumed to be possible through the currently documented G7 Pro configuration protocol.

The project must determine which portions can be implemented through:

1. Persistent G7 Pro hardware configuration
2. Controller firmware capabilities
3. G7Forge runtime translation
4. A combination of the above

The final implementation should be based on experimentally verified behavior rather than assumptions from GameSir Nexus, Steam Input, or other controller software.