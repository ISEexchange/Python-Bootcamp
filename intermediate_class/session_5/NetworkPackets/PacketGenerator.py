
from Packet import Packet


class PacketGenerator(object):

    """ Produce generator objects"""

    def __init__(self):
        pass

    def generate_packets(self):
        """ Generate a brand new packet object forever """
        while True:
            new_packet = Packet()
            new_packet.fill_in_values()
            yield new_packet
