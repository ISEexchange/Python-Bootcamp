#################################
# In Class Assignment and Homework
#################################

# 1. Create a PacketServer class that uses SocketServer (its purpose is to
#    provide packets to some client over the network)
# 2. Everytime a client connects to the server, the server should verify that
#    the client is asking for a packet and then it should send it a Packet object.
# 3. PacketServer should have a function called make_packet() which is called
#    to create the packet object for the client.
# 4. PacketServer should create its packets using a generator.
# 5. The client should be class based.
# 6. The client should connect to the server using a socket, at a specified
#    ip/port.
# 7. The client should tell the server it wants a packet with some string
#    indicating so.
# 8. Add prints in the server and client to show whats happening.

# See PacketTester.py in the NetworkPackets directory and call it by:
#     python PacketTester.py
