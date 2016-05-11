
import pickle
import socket
import Globals as G


class PacketClient(object):

    """ """

    def __init__(self):
        self.ip = G.IP
        self.port = G.PORT
        self.server_connection = None

    def connect(self):
        """ """
        self.server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_connection.connect((self.ip, self.port))
        print 'PacketClient: I\'m connected to the server'

    def ask_server_for_data(self):
        """ """
        if self.server_connection:
            print 'PacketClient: I\'m asking the server for a packet'
            self.server_connection.send("i need a packet")
            server_data = self.server_connection.recv(1024)
            server_packet = pickle.loads(server_data)
            print 'PacketClient: I got the following from the server'
            print server_packet
