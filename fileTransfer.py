import time

currentFile = None

def client_send(fileName):
    import TSC.client as clt
    with open(fileName, 'r') as file:
        for charactor in file.read():
            success = clt.send(f"FILE#|#{fileName}#|#SEND#|#{charactor}")
        clt.send(f"FILE#|#{fileName}#|#stop")

def client_recv(data):
    data = data.split("#|#")
    if len(data) == 0:
        return False
    else:
        with open(data[1], "a") as file:
            file.write(data[2])



def server_rcv(data):
    if data is None:
        return False
    data = data.split("#|#")
    if data[0] == "FILE":
        if data[2] == "SEND":
            with open(data[1], "a") as file:
                file.write(data[3])

def server_send(conn, filename):
    import TSC.server as ser
    with open(filename, r) as file:
        file = file.read()
    
    for letter in file:
        ser.send(conn, f"FILE#|#{filename}#|#{letter}")