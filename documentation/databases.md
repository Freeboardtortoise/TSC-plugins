## TSC-databses
this is a simplified database manager that uses a key, value system.
please use the extension .tscdb for best performance
you will find all of the commands bellow and what they do

### Datatypes
1. string: for lists of letters
2. int: for whole numbers
3. float: for numbers with decimal points

### importing the plugin
import TSC.plugins.databases as databases

### making a connection
conn = databases.Connection(_your filename_)

### verifying a database file
conn.verify()

### Making a table
conn.make_table(_table name_)

### writing to a TSC-databse
conn.add_value(_table_,_key_,_value_, _optional: datatype_)

NB: the default datatype is 'string'

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

### getting a list of all of the tables
conn.get_tables

the nice thing about TSC-databases is that there is no need to close the connection only to use conn.write() to make the changes