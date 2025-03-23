import TSC_server
def client_threaded(conn, addr, ID):
    print(f"hello {conn}")
    while True:
        data = TSC_server.recieve(conn)
        TSC_server.send(conn, "Tortoises are clever and fast")