import encrypter as e
import databases as database
conn = database.Connection('TSC/plugins/server_files/database.tdb')
conn.clear()
conn.reset()
passphrase = e._generate_passphrase()
conn.encrypt_database(passphrase=passphrase)
conn.make_table("Tortoise table")
conn.add_value(table="Tortoise table",  key="Tortoise name",  value="Tom tortoise")
conn.verify()
conn.write()
conn.encrypt_database(passphrase=passphrase)
read = conn.read(table='Tortoise table')
print(read)