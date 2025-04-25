def _generate_passphrase(passfile=None, password=None):
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
    if not password:
        random.shuffle(letters)
        letters = "".join(letters)
    else:
        output = []
        for letter in password:
            if letter not in output:
                output.append(letter)

        for letter in letters:
            if letter in output:
                pass
            else:
                output.append(letter)
        letters = "".join(output)
    if passfile is None:
        return letters
    else:
        with open(passfile, 'w') as file:
            file.write(letters)
        return 0

def encrypt(passphrase=None, passfile=None, string='', shift=1):
    # setting up the passphrase as letters
    if passfile is not None:
        with open(passfile, 'r') as file:
            file_contents = file.read()
        letters = file_contents
    else:
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
        if not blank_done:
            output = output + blank
    return output
def decrypt(passphrase=None, passfile=None, string='', shift=1):
    # setting up the passphrase as letters
    if passfile is not None:
        with open(passfile, 'r') as file:
            file_contents = file.read()
        letters = file_contents
    elif passphrase is not None:
        letters = passphrase
    else:
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
        if not blank_done:
            output = output + blank
    return output