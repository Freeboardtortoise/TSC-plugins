# How to use the TSC plugins

## console

### init
import TSC.plugins.console
TSC.plugins.console.init()

### other important information
the quit command returns False you can do what you whant with this output

###  running an initiration of the terminal interface
TSC.plugins.console.console_thing(connections)

## usernames
this is a plugin that allows you to match IP addresses to usernames
### NB
all of this information is saved in a file in the TSC/plugins/server_files/usernames.txt

### init
import TSC.plugins.usernames
TSC.plugins.usernames.init( _name of server_ )

### getting a username from the usernames plugin
TSC.plugins.usernames.get_username(_IP_)

### setting a username
TSC.plugins.usernames.set_username(_IP address_ , _username_)
