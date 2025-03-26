import TSC.server
import TSC.client
import time
import random

connections = []
def init():
    global connections
    print("this project uses the TSC-console extension made by Philip G Hall")

def console_thing(connections):
    command = input(">>>")

    commandSections = len(command.split(" "))
    if commandSections == 1:
        if command == "help":
            print("command list")
            print("help                 lists all commands")
            print("kick <ip>            removes a person from the server")
            print("send <ip> <what>     sends a message to a person on the server")
            print("quit                 quits the program")
            print("custom               can be programmed to do anything you like it to do")
        if command == "list":
            for connection in connections:
                print(f"ipv4: {str(connection[1])}, ID: {str(connection[2])}")
    elif commandSections == 2:
        if command.split(" ")[0] == "kick":
            for connection in connections:
                if (connection[1])[0] == command.split(" ")[1]: #conn, addr, ID
                    conn = connection[0]
                    conn.close()
    elif commandSections == 3:
        if command.split(" ")[0] == "send":
            for connection in connections:
                if connection[1][0] == command.split(" ")[1]:
                    conn = connection[0]
                    TSC.server.send(conn, command[2])
    
    elif command == "quit":
        quit()
    elif command == "custom":
        return True
    elif command == "clear":
        print("\n"*50)