import TSC.server
import TSC.plugins.server_console
import _thread
TSC.server.init("127.0.0.1")
TSC.plugins.server_console.init()

running = True
TSC.server.get_clients_threaded()
while running:
    connections = TSC.server.get_connections()

    TSC.plugins.server_console.server_console(connections)