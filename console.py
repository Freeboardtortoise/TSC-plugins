import TSC.server
import TSC.client

connections = []
importedThings = []
def init():
    global connections,  importedThings
    print("this project uses the TSC-console extension made by Philip G Hall")
    file = open("TSC/plugins/plugins.txt","r")
    for line in (file.read()).split("\n"):
        if line == "usernames":
            import usernames
            importedThings = importedThings + ["usernames"]
        else:
            pass
    file.close()

def console_thing(connections):
    global importedThings
    command = input(">>>")

    commandSections = len(command.split(" "))
    if commandSections == 1:
        if command == "help":
            print("command list")
            print("help                 lists all commands")
            if "usernames" in importedThings:
                print("kick <username>    remove a person from the server")
                print("send <username>    sends the person sellected a message")
            else:
                print("kick <ip>            removes a person from the server")
                print("send <ip> <what>     sends a message to a person on the server")
            print("quit                 quits the program")
        if command == "list":
            for connection in connections:
                if "usernames" in importedThings:
                    import TSC.plugins.usernames as usernames
                    print(f"ipv4: {str(connection[1])}, ID: {str(connection[2])}, Username: {usernames.get_username(connection[1])}")
                else:
                    print(f"ipv4: {str(connection[1])}, ID: {str(connection[2])}")
    elif commandSections == 2:
        if command.split(" ")[0] == "kick":
            for connection in connections:
                if "usernames" in importedThings:
                    import TSC.plugins.usernames as usernames
                    if connection[1][0] == usernames.get_username(command.split(" ")[1]):
                        conn = connection[0]
                        conn.close()
                else:
                    if (connection[1])[0] == command.split(" ")[1]: #conn, addr, ID
                        conn = connection[0]
                        conn.close()
    elif commandSections == 3:
        if command.split(" ")[0] == "send":
            for connection in connections:
                if "usernames" not in importedThings:
                    import TSC.plugins.usernames as usernames
                    if connection[1][0] == command.split(" ")[1]:
                        conn = connection[0]
                        TSC.server.send(conn, command[2])
                else:
                    if connection[1][0] == usernames.get_username(command.split(" ")[1]):
                        conn = connection[0]
                        TSC.server.send(conn, command[2])
    
    elif command == "quit":
        return False
    elif command == "custom":
        return True
    elif command == "clear":
        print("\n"*50)
