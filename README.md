# How to use the TSC plugins

## console

### init
import TSC.plugins.console
TSC.plugins.console.init()

### other important information
the quit command returns False from console_thing you can do what you want with this output

###  running an initiration of the terminal interface
TSC.plugins.console.console_thing(connections)

## usernames
this is a plugin that allows you to match IP addresses or ID's to usernames
### NB
all of this information is saved in a file in the TSC/plugins/server_files/usernames.txt

### init
import TSC.plugins.usernames
TSC.plugins.usernames.init()

### getting a username from the usernames plugin
TSC.plugins.usernames.get_username(_IP or ID)

### setting a username
TSC.plugins.usernames.set_username(_IP_or ID, _username_)

## TSC-databses

### importing the plugin
import TSC.plugins.databses

### making a connection
conn = TSC.plugins.databases.Connection(filename=_your filename_)

### verifying a database file
conn.verify()

### Making a table
conn.make_table(_table name_)

### writing to a TSC-databse
conn.add_value(_table_,_key_,_value_)
editing values

### reading from a TSC-database
conn.read(_optional: table_,_optional: value_)

### commiting/writing the changes
conn.write()

### closing the connection
conn.close()

### clearing the database of all entries
conn.clear()

### reset connection back to origonal before opening
conn.reset()