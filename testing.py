import encrypter as e
passfile = "passfile.txt"
encrypted = e.encrypt(passfile=passfile, string="Clever tortoise")
decrypted = e.decrypt(passfile=passfile, string=encrypted)
print(encrypted)
print(decrypted)