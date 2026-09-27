class TurboConfig:

    """

    Represents Turbo configuration for a controller input.

    """

    def __init__(self, button):

        self.button = button

        self.enabled = False

        self.level = 0

        self.mode = "hold"

    def enable(self, level=1):

        self.enabled = True

        self.level = level

    def disable(self):

        self.enabled = False

    def set_mode(self, mode):

        if mode not in ("hold", "toggle"):

            raise ValueError("Turbo mode must be 'hold' or 'toggle'")

        self.mode = mode