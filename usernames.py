import TSC.client
import TSC.server

def init(server_name):
    #opens and adds the server name to the server_info.txt file
    file = open("TSC/plugins/server_files/server_info.txt", "w")
    file.write(f"name, {server_name}\n")
    file.close()
    #clears the usernames.txt file
    file = open("TSC/plugins/server_files/usernames.txt", "w")
    file.write("")
    file.close()

def get_username(addr):
    #opens and reads the usernames.txt file
    file = open("TSC/plugins/server_files/usernames.txt", "r")
    file_contents = file.read()
    file.close()
    file = file_contents
    what_to_return = ""
    #ititares over each line and checks for them
    for line in file.split("\n"):
        line = line.split(",")
        if line[0] == addr:
            what_to_return = line[1]
    
    #returns the correct thing
    if what_to_return == "":
        return None
    else:
        return what_to_return

def set_username(addr, username):
    #checking if username is already in database
    file = open("TSC/plugins/server_files/usernames.txt", "r")
    for line in file.read():
        line = line.split(",")
        if line[0] == addr:
            file.close()
            return False
    file.close()

    #adding to the file the username and the address
    try:
        file = open("TSC/plugins/server_files/usernames.txt", "a")
        file.write(f"{addr},{username}\n")
        file.close()
        return True
    except:
        return False