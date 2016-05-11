
import random


class Packet(object):

    """ Class for encapsulating info about a packet """

    def __init__(self):
        self.header  = None
        self.data    = None
        self.trailer = None

    def fill_in_values(self):
        """ Randomize the data attributes """
        self.header  = random.randint(0, 1000)
        self.data    = random.randint(0, 100000)
        self.trailer = random.randint(0, 1000)

    def __str__(self):
        """ Return a nice string for printing """
        return 'Header: %s\nData: %s\nTrailer: %s\n' % (
            self.header, self.data, self.trailer)
