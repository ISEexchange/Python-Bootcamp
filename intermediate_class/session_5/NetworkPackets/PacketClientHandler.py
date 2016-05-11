
import pickle
from SocketServer import BaseRequestHandler
from PacketGenerator import PacketGenerator


class PacketClientHandler(BaseRequestHandler):

    """ """

    def handle(self):

        """ This function will be called whenever a client message arrives """

        self.data = self.request.recv(4096).strip()
        if self.data == 'i need a packet':
            print 'PacketClientHandler: I\'ve been asked for a packet'
            self.pkt_gen = PacketGenerator().generate_packets()
            new_packet = self.pkt_gen.next()
            packet_str = pickle.dumps(new_packet, -1)
            print 'PacketClientHandler: Sending client a packet'
            self.request.sendall(packet_str)
