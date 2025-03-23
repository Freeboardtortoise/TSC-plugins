import TSC_client

TSC_client.init('127.0.0.1')
print("Welcome to TSC testing")
print("client side ")
running = True
tortoise = TSC_client.send("Tortoise")
print(tortoise)