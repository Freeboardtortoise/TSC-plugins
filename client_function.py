import TSC_server
def client_threaded(conn, addr, ID):
    print(f"hello {conn}")
    while True:
        data = TSC_server.recieve(conn)
        print(data)
        if data == "Tortoise":
            print("Yes tortoise")
        print(addr)
        TSC_server.send(conn, "Tortoises are clever and fast")