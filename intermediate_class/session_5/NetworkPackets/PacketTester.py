
import time
import threading
from PacketServer import PacketServer
from PacketClient import PacketClient


def launch_server():
    PacketServer()

new_thread = threading.Thread(target=launch_server)
new_thread.start()

time.sleep(2)
client = PacketClient()
client.connect()
client.ask_server_for_data()
