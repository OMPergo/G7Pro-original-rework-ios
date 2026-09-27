class BaseTransport:

    """

    Defines the basic communication interface used by G7Forge.

    """

    def connect(self):

        raise NotImplementedError

    def disconnect(self):

        raise NotImplementedError

    def read(self):

        raise NotImplementedError

    def write(self, data):

        raise NotImplementedError

    @property

    def connected(self):

        raise NotImplementedError