import databases
conn = databases.Connection("database.tdb")

conn.add_table("tortoise table 1")
conn.remove_table("tortoise table 1")
conn.add_table("tortoise table")
conn.add_value("tortoise table", "name", "Darion")
conn.add_value("tortoise table", "age", 100, "int")
conn.verify()
conn.write()
conn.close()

conn = databases.Connection("database.tdb")
conn.remove_value(table="tortoise table", key="name")
conn.verify()
conn.write()
print(conn.read())