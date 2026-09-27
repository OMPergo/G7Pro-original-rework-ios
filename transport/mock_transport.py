from .base_transport import BaseTransport

class MockTransport(BaseTransport):

    """

    Simulates a G7 Pro connection for development and testing.

    """

    def __init__(self):

        self._connected = False

        self._data = bytearray()

    def connect(self):

        self._connected = True

    def disconnect(self):

        self._connected = False

    def read(self):

        if not self._connected:

            raise RuntimeError("Transport is not connected")

        return bytes(self._data)

    def write(self, data):

        if not self._connected:

            raise RuntimeError("Transport is not connected")

        self._data = bytearray(data)

    @property

    def connected(self):

        return self._connected