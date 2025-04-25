import encrypter as e
passfile = "passfile.txt"

if e._generate_passphrase(passfile=passfile) == True:
    encrypted = e.encrypt(passfile=passfile, string="Tortoises are fast and clever")
    decrypted = e.decrypt(passfile=passfile, string=encrypted)
    print(encrypted)
    print(decrypted)
else:
    print("falied")