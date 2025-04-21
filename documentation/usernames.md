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