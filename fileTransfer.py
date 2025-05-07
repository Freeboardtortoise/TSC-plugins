import time

currentFile = None
currentFiles = []
files_started = []

def client_send(fileName):
    import TSC.client as clt
    clt.send(f"FILE#|#{fileName}#|#START")
    with open(fileName, 'r') as file:
        for charactor in file.read():
            success = clt.send(f"FILE#|#{fileName}#|#SEND#|#{charactor}")
    clt.send(f"FILE#|#{fileName}#|#stop")
    return True


def server_rcv(data):
    if data is None:
        return False
    data = data.split("#|#")
    if data[0] == "FILE":
        if data[2] == "SEND":
            with open(data[1], "a") as file:
                file.write(data[3])

def server_send(conn, fileName):
    import TSC.server
    with open(fileName, "r") as file:
        file = file.read()
    TSC.server.send(conn, f"FILE#|#{fileName}#|#START")
    for numberm, letter in enumerate(file):
        TSC.server.send(conn, f"FILE#|#{fileName}#|#{number}#|#{letter}")
    TSC.server.send(conn, f"FILE#|#{fileName}#|#END")

def client_recv():
    global currentFiles, files_started
    import TSC.client as client
    latest = client.get_messages_all()
    for line in latest:
        line_parts = line.split("#|#")
        if line_parts[0] != "FILE":
            pass
        
        if line_parts[2] == "START":
            if line_parts[2] in files_started:
                pass
            else:
                files_started.append(line_parts[1])
            
        if line_parts[2] == "SEND" and len(line_parts) >= 4:
            fileName = line_parts[1]
            charactor = line_parts[3]
            charactor_number = line_parts[2]
            currentFiles.append([fileName, len(currentFiles), charactor])

def client_writeFile(file_to_write): 
    global currentFiles, files_started
    
    if file_to_write not in files_started:
        print("Messages have been cleared, there is no way to write the file whole")
        return False
    
    # Clear the file first
    open(file_to_write, "w").close()
    
    # Write all characters for this file
    with open(file_to_write, "a") as output_file:
        for entry in currentFiles:
            fileName = entry[0]
            if fileName == file_to_write:
                charactor = entry[2]
                output_file.write(charactor)
    
    return True
