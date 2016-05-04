#################################
# In Class Assignment and Homework
#################################

# 1. Create a class called Packet that contains:
#        - header  - integer
#        - data  - integer
#        - trailer  - integer
#        - fill_in_values() - function

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

# 2. Create a class called PacketGenerator that contains:
#        - generate_packets() - function generator
#            - this function yields a packet object on request

class PacketGeneratorMaker(object):

    """ Produce generator objects"""

    def __init__(self):
        pass

    def generate_packets(self):
        """ Generate a brand new packet object forever """
        while True:
            new_packet = Packet()
            new_packet.fill_in_values()
            yield new_packet


# 3. In main, instantiate a PacketGenerator. Generate packets in a while loop.
#    Print the contents of the packet

if __name__ == "__main__":

    pgm = PacketGeneratorMaker()

    generator_object = pgm.generate_packets()

    counter = 1
    for _ in xrange(10):
        new_packet = generator_object.next()
        print 'New Packet #%d' % counter
        print '    h=%s d=%s t=%s\n' % (new_packet.header,
            new_packet.data, new_packet.trailer)
        counter += 1
