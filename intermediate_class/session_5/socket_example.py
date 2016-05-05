import socket
import json
import threading
import time


class SocketServer():
    """ Open a socket and listen forever for client data """

    def __init__(self):
        self.socket = None
        self.port = 42448
        self.establish_socket()
        self.launch_listener()

    def establish_socket(self):
        """ Bind to the socket """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('0.0.0.0', self.port))

    def launch_listener(self):
        """ Launch the listener function in its own thread """
        new_thread = threading.Thread(target=self.listen)
        new_thread.start()

    def listen(self):
        """ Forever listen and accept new connections from clients """
        print 'Listening on %s:%s for clients' % ('0.0.0.0', self.port)

        while True:
            try:
                # Argument is number of queued clients
                self.socket.listen(1)
                # Accept new connections (blocking) when they come in
                conn, addr = self.socket.accept()

                # Get tuple of (hostname, aliaslist, ipaddrlist)
                details = socket.gethostbyaddr(addr[0])
                print "\nConnected with ip: %s (%s), port: %s" % (addr[0], details[0], addr[1])
                client_data = conn.recv(1024)

                if client_data:
                    # If there was a problem processing this client's data, continue
                    # to next iteration of while loop - do not exit just because one
                    # client sent bad data
                    try:
                        self.process_raw_data(conn, client_data)
                    except Exception, e:
                        print e
                        continue
                else:
                    print "Connection Closed By Client"

            except Exception, e:
                print e
                conn.close()

    def process_raw_data(self, client_conn, data):
        """ Process the raw command that was sent by a client """
        # Try to decode the data from the client. If this fails, then the
        # client did not send JSON data. Tell the client about the error.
        try:
            json_data = json.loads(data)
        except Exception, e:
            print "Exception:", e
            client_conn.sendall(str(e))
            raise e
        print "From Client, JSON Data:", json_data


if __name__ == "__main__":

    s = SocketServer()

    time.sleep(3)

    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'
    port = 42448
    client.connect((host, port))

    data = json.dumps({"hello": "world"})
    client.send(data)
