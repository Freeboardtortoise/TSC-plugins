import TSC_server


def client():
    print("hello user")


TSC_server.init("127.0.0.1")

running = True
while running:
    TSC_server.get_clients()