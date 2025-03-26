import TSC.server
import console
TSC.server.init('127.0.0.1')
console.init()

running = True
TSC.server.get_clients_threaded()
while running:
    action = console.console_thing(TSC.server.get_connections())
    if action == False:
        running = False