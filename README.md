# What is TSC-plugins

this is a collection of all of the official plugins

this is the list of plugins and the developers

- console Freeboardtortoise
- usernames Freeboardtortoise
- databases Freeboardtortoise
- encrypter Freeboardtortoise

## how to import plugins

add the name of your plugin to the plugins.txt file on a new line
and make sure your plugin file is in the TSC.plugins directory
import your file into your program

## console

### import and initialise TSC-console

```
import TSC.plugins.console as console
console.init()
```

### running the console

```
console.console_thing(TSC.server.get_connections)
```

## encrypter

### importing and initialising TSC-encrypter

```
import TSC.plugins.encrypter as _e
```

### making a passphrase

```
passphrase = _e.generate_passphrase()
```

### making a passfile

```
_e.generate_passphrase(passfile="filename.txt")
```

### encrypting a string

```
_e.encrypt(passphrase="passphrase",passfile="filename.txt",string="string to encrypt",  shift=1)
```

### decrypt a string

```
_e.decrypt(pssphrase="passphrase",passfile="filename.txt",string="string to decrypt", shift=1)
```

## usernames

### how to import TSC-usernames

```
import TSC.plugins.usernames as usernames
usernames.init("path to usernames file")
```

### setting a username

```
usernames.set_username(addr=addr, username="username")
```

### getting a username

```
username = usernames.get_username(addr=addr)
```

## TSC-databases

### importing TSC-databases

```
import TSC.plugins.databases as databases
```

### initialising a connection

```
conn = databases.Connection("databases.tdb")
```

### adding a table

```
conn.add_table(name="table name")
```

### adding a value

there are 3 datatypes for values:

- string (for strings and charactors)
- int (for whole numbers)
- float (for floats/reals)
  these are set in the datatype argument

```
conn.add_value(table="table name", key="key", value="value", datatype="string")
```

### verify database (required for writing to it)

is is very important that you dont just do this: self.valid=True becuase the verify process makes sure that it does not run into errors later when reading

```
conn.verify()
```

### write to the database

this secures changes into the database
NB: no changes will be reflected until you run this

```
conn.write()
```

### read from the database

```
conn.read(table="table name", key="key")
```

if nothing is provided for _table_:
you will recieve all of the information in the table
if nothing is provided for _key_ and _table_ contains a valid table:
you will recieve all of the information from that table
if _table_ contains a valid table and _key_ contains a valid key from that table:
you will recieve the value

### editing values in the database

```
conn.edit_value(table="table name", key="key", value="new_value")
```

all of the arguments are required

### getting a list of all tables

```
tables = conn.get_table_list()
```

### encrypting the database

```
# TSC-encrypter must be installed
conn = databases.Connection("database.tdb", encrypt=True, passphrase="passphrase", passfile="passfile.txt") #one of the passphrase or passfile is required and not the other
```

this is another way of opening the connection

### removing from the database

removing an entire table

```
conn.remove_table(table="table name")
```

removing a key from a table

```
conn.remove_value(table="table name", value="value")
```
