
def pack_command(command):
    splitter = "##|##|##|##"
    output = ''

    for item, number in enumerate(command):
        if item == 0:
            pass
        else:
            output = output + splitter
    
    return output

def unpack_command(string):
    splitter = "##|##|##|##"
    output = []
    output = string.split(splitter)
    return output