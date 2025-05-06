import TSC.server as server
import fileTransfer as ft
server.init("127.0.0.1")
server.get_clients_threaded()
while True:
    pass