class Profile:

    """

    Represents a G7 Pro controller configuration profile.

    """

    def __init__(self, profile_number):

        self.profile_number = profile_number

        self.remappings = {}

        self.turbo = {}

        self.stick_settings = {}

        self.trigger_settings = {}

        self.mnk_settings = {}

    def set_remap(self, source, target):

        self.remappings[source] = target

    def set_turbo(self, button, enabled):

        self.turbo[button] = enabled

    def set_stick_setting(self, name, value):

        self.stick_settings[name] = value

    def set_trigger_setting(self, name, value):

        self.trigger_settings[name] = value

    def set_mnk_setting(self, name, value):

        self.mnk_settings[name] = value