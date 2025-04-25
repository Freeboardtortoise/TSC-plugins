import time
import random

def _generate_passphrase(passfile=None):
    import random
    letters = ["q","w","e","r","t","y",
                "u","i","o","p","a","s",
                "d","f","g","h","j","k",
                "l","z","x","c","v","b",
                "n","m","!","@","#","$",
                "%","^","&","*","(",")",
                "[","]","{","}","|","\\",
                "~","`","-","=","_","+",
                "Q","W","E","R","T",
                "Y","U","I","O","P","A",
                "S","D","F","G","H","J",
                "K","L","Z","X","C","V",
                "B","N","M"," ","1","2",
                "3","4","5","6","7","8",
                "9","0"]
    random.shuffle(letters)
    letters = "".join(letters)
    if passfile == None:
        return letters
    else:
        with open(passfile, 'w') as file:
            file.write(letters)
        return True

def encrypt(passphrase=None, passfile=None, string='', shift=1):
    # setting up the passphrase as letters
    if passfile != None:
        with open(passfile, 'r') as file:
            file_contents = file.read()
        letters = file_contents
    elif passphrase != None:
        letters = passphrase

    elif passphrase == None and passfile == None:
        print("ERROR")
        print("NO PASSFILE OR PASSPHRASE PROVIDED")
        return None
    output = ''
    for blank in string:
        blank_done = False
        for number, letter in enumerate(letters):
            if not blank_done:
                if blank == letter:
                    number = number + shift
                    if number > len(letters) - 1:
                        number = number % (len(letters))
                    output = output + letters[number]
                    blank_done = True
        if blank_done == False:
            output = output + blank
    return output
def decrypt(passphrase=None, passfile=None, string='', shift=1):
    # setting up the passphrase as letters
    if passfile != None:
        with open(passfile, 'r') as file:
            file_contents = file.read()
        letters = file_contents
    elif passphrase != None:
        letters = passphrase
    elif passphrase == None and passfile == None:
        print("ERROR")
        print("NO PASSFILE OR PASSPHRASE PROVIDED")
        return None

    output = ''
    for blank in string:
        blank_done = False
        for number, letter in enumerate(letters):
            if not blank_done:
                if blank == letter:
                    number = number - shift
                    if number < 0:
                        number = number % (len(letters))
                    output = output + letters[number]
                    blank_done = True
        if blank_done == False:
            output = output + blank
    return output