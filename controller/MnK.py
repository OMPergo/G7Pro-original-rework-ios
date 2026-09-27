class MNKConfig:

    """

    Represents Mouse and Keyboard configuration for the G7 Pro.

    """

    def __init__(self):

        self.enabled = False

        self.keyboard_bindings = {}

        self.mouse_bindings = {}

        self.mouse_sensitivity_x = 1.0

        self.mouse_sensitivity_y = 1.0

        self.deadzone = 0.0

        self.response_curve = 1.0

        self.smoothing = 0.0

        self.output_mode = "unknown"

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False

    def bind_keyboard(self, key, output):

        self.keyboard_bindings[key] = output

    def bind_mouse(self, button, output):

        self.mouse_bindings[button] = output

    def set_sensitivity(self, x, y):

        self.mouse_sensitivity_x = x

        self.mouse_sensitivity_y = y

    def set_deadzone(self, value):

        self.deadzone = value

    def set_response_curve(self, value):

        self.response_curve = value

    def set_smoothing(self, value):

        self.smoothing = value