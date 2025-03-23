import TSC.server
def client_threaded(conn, addr, ID):
    connected = True
    while connected:
        TSC.server.recieve(conn)
    return False