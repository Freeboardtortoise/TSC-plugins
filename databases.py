def _intify(string):
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    for letter in string:
        if letter in numbers:
            pass
        else:
            return None

    return int(string)

def _is_int(number):
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    for letter in str(number):
        if letter in numbers:
            pass
        else:
            return False
    return True

def _is_float(string):
    numbers = ['1','2','3','4','5','6','7','8','9','0','.']
    for letter in str(string):
        if letter in numbers:
            pass
        else:
            return False

    return True

def _floatify(string):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
    for letter in string:
        if letter in numbers:
            pass
        else:
            return None

    return float(string)

def _check_file(filename):
    try:
        open(filename, 'r').close()
        return True
    except:
        return False

class Connection:
    def __init__(self, filename, encrypt=False, passphrase=None, passfile=None):
        if encrypt:
            if _check_file("TSC/plugins/encrypter.py") == True:
                self.encrypt = True
                if passfile != None:
                    with open(passfile,"r") as file:
                        self.passphrase = file.read()
                elif passphrase != None:
                    self.passphrase = passphrase
            else:
                print("ERROR")
                print("encrypter package not installed or not in the correct directory")
                print("install all pugins from the following commands")
                print("git clone https://github.com/Freeboardtortoise/TSC-plugins.git")
                print("then move all of them into the plugins directory in TSC/plugins")
        self.file = filename
        self.valid = False
        self.splitter = "$|$"
        self.values = []
        self.tables = []
        self.encrypt = encrypt
        if self.encrypt:
            pass
        else:
            self.passphrase = None
        open(filename, 'a').close()
        file = open(filename, 'r')
        file_len = file.read()
        file.close()
        # validating
        if file_len == 0:
            file.write('TSC-database=validated')
            self.valid = True
        with open(filename, 'r') as file:
            file = file.read()
            file = file.split("\n")
            for line in file:
                line = line.split(self.splitter)
                if line[0] == "TABLE":
                    if line[1] == "NEW":
                        if self.encrypt == False:
                            self.tables.append(line[2])
                        else:
                            import TSC.plugins.encrypter as e
                            self.tables.append(e.decrypt(string=line[2], passphrase=self.passphrase))
                    if line[2] == "VALUE":
                        if line[3] == "STRING":
                            if self.encrypt == False:
                                self.values.append([line[1], line[3], line[4]])
                            else:
                                import TSC.plugins.encrypter as e
                                table = e.decrypt(string=line[1], passphrase=self.passphrase)
                                key = e.decrypt(string=line[3], passphrase=self.passphrase)
                                value = e.decrypt(string=line[4], passphrase=self.passphrase)
                                self.values.append([table, key, value])
                        elif line[3] == "INT":
                            if self.encrypt == False:
                                table, key, value = line[1], line[3], line[4]
                                value = _intify(value)
                                if value == None:
                                    print("invalid datatype")
                                    return 0
                                else:
                                    self.values.append([table, key, value])
                            else:
                                import TSC.plugins.encrypter as e
                                table = e.decrypt(string=line[1], passphrase=self.passphrase)
                                key = e.decrypt(string=line[3], passphrase=self.passphrase)
                                value = e.decrypt(string=line[4], passphrase=self.passphrase)
                                value = _intify(value)
                                self.values.append([table, key, value])
                        elif line[3] == "FLOAT":
                            if self.encrypt == False:
                                table, key, value = line[1], line[3], line[4]
                                value = _floatify(value)
                                if value == None:
                                    print("invalid datatype")
                                    return 0
                                else:
                                    self.values.append([table, key, value])
                            else:
                                import TSC.plugins.encrypter as e
                                table = e.decrypt(string=line[1], passphrase=self.passphrase)
                                key = e.decrypt(string=line[3], passphrase=self.passphrase)
                                value = e.decrypt(string=line[4], passphrase=self.passphrase)
                                value = _floatify(value)
                                self.values.append([table, key, value])

    def add_table(self, name):
        if name in self.tables:
            print("ERROR")
            print(f"TABLE: {name} already exists")
            quit()
        else:
            self.tables = self.tables + [name]
            return 0

    def clear(self):
        try:
            open(self.file, "w").close()
            return 0
        except:
            return 1

    def add_value(self, table, key, value, datatype='string'):
        if datatype.lower() == 'string':
            for theValue in self.values:
                if theValue[0] == table:
                    if theValue[1] == key:
                        return False
            self.values = self.values + [[table, key, value, "STRING"]]
            return True
        elif datatype.lower() == 'int':
            for theValue in self.values:
                if theValue[0] == table:
                    if theValue[1] == key:
                        return False
            self.values = self.values + [[table, key, value, "INT"]]
            return True
        elif datatype.lower() == 'float':
            for theValue in self.values:
                if theValue[0] == table:
                    if theValue[1] == key:
                        return False
            self.values = self.values + [[table, key, value, "FLOAT"]]
            return True
        else:
            return False

    def verify(self):
        with open(self.file, 'r') as file:
            file = file.read()
            file = file.split("\n")
            file = file[1:]
            for number, line in enumerate(file):
                file[number] = line.split(self.splitter)
        self.valid = True
        for value in self.values:
            if value[3] == "INT":
                if _is_int(value[2]) == True:
                    self.valid = True
            elif value[3] == "FLOAT":
                if _is_float(value[2]) == True:
                    self.valid = True

        return True

    def write(self):
        if self.valid:
            with open(self.file, 'w') as file:
                if self.valid == True:
                    file.write("TSC-database=validated\n")
                for table in self.tables:
                    if self.encrypt == True:
                        import TSC.plugins.encrypter as e
                        file.write(f"TABLE{self.splitter}NEW{self.splitter}{e.encrypt(string=table, passphrase=self.passphrase)}\n")
                    else:
                        file.write(f"TABLE{self.splitter}NEW{self.splitter}{table}\n")
                for value in self.values:
                    if self.encrypt == True:
                        table = e.encrypt(string=value[0], passphrase=self.passphrase)
                        key = e.encrypt(string=value[1], passphrase=self.passphrase)
                        if value[3] == "STRING":
                            _value = e.encrypt(string=value[2], passphrase=self.passphrase)
                        elif value[3] == "INT":
                            _value = e.encrypt(string=str(value[2]), passphrase=self.passphrase)
                        elif value[3] == "FLOAT":
                            _value = e.encrypt(string=str(value[2]), passphrase=self.passphrase)
                        file.write(f"TABLE{self.splitter}{table}{self.splitter}VALUE{self.splitter}{key}{self.splitter}{_value}{self.splitter}{value[3]}\n")
                    else:
                        file.write(f"TABLE{self.splitter}{value[0]}{self.splitter}VALUE{self.splitter}{value[1]}{self.splitter}{value[2]}{self.splitter}{value[3]}\n")
        else:
            print("ERROR")
            print("INVALID DATABASE")
            print("VERIFY DATABASE WITH conn.verify()")
            quit()

    def read(self, key=None, table=None):
        returnedValues = []
        if table == None and key == None:
            for value in self.values:
                returnedValues.append(value[:3])
        elif key == None and table != None:
            for value in self.values:
                if value[0] == table:
                    returnedValues = returnedValues + [[value[1],value[2]]]
        elif key != None and table == None:
            for value in self.values:
                if value[1] == key:
                    returnedValues.append(value[2])
        elif key != None and table != None:
            for value in self.values:
                if value[0] == table:
                    if value[1] == key:
                        return value[2]
                    else:
                        pass
        return returnedValues

    def edit_value(self, table, key, value):
        for number, sellectedValue in enumerate(self.values):
            if sellectedValue[0] == table:
                if sellectedValue[1] == key:
                    self.values[number][2] = value
                    return True
                print("ERROR")
                print("NO SUTCH value in table")
                return 1
            print("ERROR")
            print("NO SUTCH TABLE")
            quit()
        print("NOTHING IN DATABASE")

    def get_table_list(self):
        return self.tables
    
    def remove_table(self, table):
        # setting the new_values and new_tables variables
        new_tables = []
        new_values = []
        # populating the new_values and new_tables varibles
        for theTable in self.tables:
            if theTable == table:
                pass
            else:
                new_tables.append(theTable)
        for value in self.values:
            if value[0] == table:
                pass
            else:
                new_values.append(value)
        # setting the self.values and self.tables to the new_tables and new_values
        self.tables = new_tables
        self.values = new_values
        return 0
    
    def remove_value(self, table, key):
        new_values = []

        for value in self.values:
            if value[0] == table and value[1] == key:
                pass
            else:
                new_values.append(value)
        
        self.values = new_values
        return 0
    
    def close(self):
        self.values = []
        self.tables = []
        self.passphrase = ""
        return 0