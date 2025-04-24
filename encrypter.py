import time
import random

def _generate_passphrase():
    import random
    letters = ["q","w","e","r","t","y",
                "u","i","o","p","a","s",
                "d","f","g","h","j","k",
                "l","z","x","c","v","b",
                "n","m","!","@","#","$",
                "%","^","&","*","(",")",
                "[","]","{","}","|","\\",
                "~","`","-","=","_","+",
                "=","Q","W","E","R","T",
                "Y","U","I","O","P","A",
                "S","D","F","G","H","J",
                "K","L","Z","X","C","V",
                "B","N","M"," ","1","2",
                "3","4","5","6","7","8",
                "9","0"]
    random.shuffle(letters)
    letters = "".join(letters)
    return letters

def encrypt(passphrase, string='', file='', shift=1):
    # setting up the passphrase as letters
    letters = passphrase
    
    if file != '':
        _file = open(file)
        string_to_encrypt = file.read()
        _file.close()
        string = string_to_encrypt
    output = ''
    for blank in string:
        blank_done = False
        for number, letter in enumerate(letters):
            if not blank_done:
                if blank == letter:
                    number = number + shift
                    if number > len(letters) - 1:
                        number = number % (len(letters) + 1)
                    output = output + letters[number]
                    blank_done = True
        if blank_done == False:
            output = output + blank
    if file != '':
        with open(file, 'w') as file:
            file.write(string)
        return None
    else:
        return output
def decrypt(passphrase, string='', file='', shift=1):
    # setting up the passphrase as letters
    letters = passphrase
    
    if file != '':
        _file = open(file)
        string_to_encrypt = file.read()
        _file.close()
        string = string_to_encrypt
    else:
        string = string
    output = ''
    for blank in string:
        blank_done = False
        for number, letter in enumerate(letters):
            if not blank_done:
                if blank == letter:
                    number = number - shift
                    if number < 0:
                        number = number % (len(letters) + 1)
                    output = output + letters[number]
                    blank_done = True
    if blank_done == False:
        output = output + blank
    return output