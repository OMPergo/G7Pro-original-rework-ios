class G7Protocol:

    """

    Handles communication with the GameSir G7 Pro protocol.

    """

    def __init__(self, transport):

        self.transport = transport

    def connect(self):

        raise NotImplementedError

    def read_profile(self, profile_number):

        raise NotImplementedError

    def write_profile(self, profile_number, data):

        raise NotImplementedError