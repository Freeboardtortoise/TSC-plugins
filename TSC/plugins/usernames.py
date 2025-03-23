import TSC.server
import time
import random

def init(server_name):
    file = open("TSC/library files/usernames.txt", "w")
    file.close()
    file = open("TSC/library files/usernames.txt", "r")
    file_contents = file.read()
    if len(file_contents) == 0:
        file.close()
        file = open("TSC/library files/usernames.txt", "w")
        file.write(f"{server_name}")
    else:
        name = file_contents.split("\n")[0]
        file.close()
        return name

def server_add_name(IP, name):
    try:
        file = open("TSC/library files/usernames.txt", "a")
        file.write(f"{IP},{name}")
        return True
    except:
        return False

def server_get_name(IP):
    try:
        file = open("TSC/library files/usernames.txt", "r")
        file_contents = file.read()
        for line in file_contents.split("\n")
            if line.split(",")[0] == IP:
                return line.split(",")[1]
        return None
    except:
        return None