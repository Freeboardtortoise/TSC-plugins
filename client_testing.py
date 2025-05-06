import TSC.client as client
import fileTransfer as fts
client.init("127.0.0.1")
client.recieve_messages()
print("starting loop")
done = False
while not done:
    fts.client_recv()
