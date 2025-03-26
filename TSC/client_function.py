import TSC.server
def client_threaded(conn, addr, ID):
    while True:
        data = TSC.server.recieve(conn)
        if data == "Connection":
            TSC.server.send(conn, "aproved")
        else:
            TSC.server.send(conn, data)

        if not data:
            print(f"disconnected from       ID: {ID}, IP address: {addr}")
            return 0