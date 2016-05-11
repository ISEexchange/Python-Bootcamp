
import SocketServer
import Globals as G
from PacketClientHandler import PacketClientHandler


class PacketServer(object):

    """ SocketServer based server which sends """

    def __init__(self):
        self.ip = G.IP
        self.port = G.PORT
        self.run()

    def run(self):
        print 'PacketServer: Starting up server'
        skt_server = SocketServer.TCPServer((self.ip, self.port), PacketClientHandler)
        skt_server.serve_forever()
