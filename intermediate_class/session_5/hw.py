#################################
# In Class Assignment and Homework
#################################

# 1. Create a PacketServer class that uses SocketServer (its purpose is to
#    provide packets to some client over the network)
# 2. Everytime a client connects to the server, the server should verify that
#    the client is asking for a packet and then it should sent it a Packet object.
# 3. PacketServer should have a function called make_packet() which is called
#    to create the packet object for the client.
# 4. PacketServer should create its packets using a generator.
# 5. The client should be class based.
# 6. The client should connect to the server using a socket, at a specified
#    ip/port.
# 7. The client should tell the server it wants a packet with some string
#    indicating so.
# 8. Add prints in the server and client to show whats happening.

# Here is some code to get you started. Break this up into separate files. One
# class per file.

# Partial server code:

class ClientHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        """ This function will be called whenever a client message arrives """
        self.data = self.request.recv(4096).strip()
        # TODO: Verify that the client is asking for a packet
        packet_obj = "<object to send to client - use pickle to picklize it first>"
        self.request.sendall(packet_obj)

skt_server = SocketServer.TCPServer((IP, PORT), ClientHandler)
skt_server.serve_forever()

# Partial client code
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
client.send("i need a packet")
client.recv(data)
