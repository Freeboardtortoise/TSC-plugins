_connections = []
def init(usernames=False):
    global usernames
    print("this project uses Tortoise server console")
    print()
    print("command list:")
    print(" help                lists command")
    print(" send <ip> <why      sends a message to the ip")
    print(" kick <ip> <why>     removes a connections from the server")
    print(" list                lists all connections")
    print(" clear               clears the screen")

def server_console(connections):
    global _connections, usernames
    _connections = connections

    command = input(">>>")
    if command.lower() == "help":
        print("command list")
        print("help             lists all commands")
        print("send <ip> <what> sends a message to the provided IP")
        print("kick <ip> <why>  removes the connection asosiated with the IP provided")
        print("list             lists all of the connections")
        print("clear            clears the screen")

    elif command.lower() == "list":
        for connection in connections:
            print(f"{connection[1]}")
    elif command.lower() == "clear":
        print("\n" * 50)