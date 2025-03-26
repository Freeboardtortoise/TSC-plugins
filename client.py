import TSC.client
import console
TSC.client.init('127.0.0.1')
console.init()

running = True
while running:
    print("connection attempt")
    input("press enter to continue")
    TSC.client.send("Connection attempt")