import time

currentFile = None

def client_send(fileName):
    import TSC.client as clt
    with open(fileName, 'r') as file:
        for charactor in file.read():
            success = clt.send(f"FILE#|#{fileName}#|#SEND#|#{charactor}")
        clt.send(f"FILE#|#{fileName}#|#stop")


def server_rcv(data):
    global isFile, size
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
    for letter in file:
        TSC.server.send(conn, f"FILE#|#{fileName}#|#{letter}")
    TSC.server.send(conn, f"FILE#|#{fileName}#|#END")

currentFiles = []
files_started = []

def client_recv():
    global currentFiles
    import TSC.client as client
    started = False
    latest = client.get_messages_all()
    for line in latest:
        line = line.split("#|#")
        if line[0] != "FILE":
            pass
        else:
            if line[2] == "END":
                return True
            if line[2] == "START":
                files_started.append(data[1])
            fileName = data[1]
            charactorNumber = data[2]
            charactor = data[3]
            currentFiles = currentFiles + [[filename, charactorNumber, charactor]]
def client_writeFile(file): 
    global currentFiles, files_started
    fileContents = ""
    fileStarted = False
    for entry in current_files:
        Filename = currentFiles[0]
        if fileName in files_started:
            pass
        else:
            print("messages has been cleared there is no way to write the file whole")
            return False
        if [fileName in files_started] and (Filename == file):
            open(Filename, "w").close()
            fileStarted = True
        if (FileName == file) and (fileStarted == True):
            data = entry[2]
            charactor = entry[1]
            with open(file, "a") as file:
                file.write(data)

def client_get_sent_file_list():
    global currentFiles
    whatToReturn = []
    for entry in currentFiles:
        fileName = entry[0]
        if filename in whatToReturn:
            pass
        else:
            whatToReturn.append(entry[0])
    return whatToReturntT
