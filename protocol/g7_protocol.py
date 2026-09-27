class G7Protocol:

    """

    Handles communication with the GameSir G7 Pro protocol.

    """

    def __init__(self, transport):

        self.transport = transport

    def connect(self):

        self.transport.connect()

        return self.transport.connected

    def disconnect(self):

        self.transport.disconnect()

        return not self.transport.connected

    def write(self, data):

        if not self.transport.connected:

            raise RuntimeError("G7 Pro is not connected")

        self.transport.write(data)

    def read_profile(self, profile_number):

        raise NotImplementedError

    def write_profile(self, profile_number, data):

        raise NotImplementedError