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
    def __init__(self, filename, _encrypt=False):
        self.file = filename
        self.valid = False
        self.splitter = "$|$"
        self.values = []
        self.tables = []
        self.encrypt = _encrypt
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

                if line[0] == "TSC-database=validated":
                    self.valid = True

    def make_table(self, name):
        if name in self.tables:
            print("ERROR")
            print(f"TABLE: {name} already exists")
            return 1
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
        if datatype == 'string':
            for theValue in self.values:
                if theValue[0] == table:
                    if theValue[1] == key:
                        return False
            self.values = self.values + [[table, key, value, "STRING"]]
            return True
        elif datatype == 'int':
            for theValue in self.values:
                if theValue[0] == table:
                    if theValue[1] == key:
                        return False
            self.values = self.values + [[table, key, value, "INT"]]
            return True
        elif datatype == 'float':
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
            file = file.pop(-1)
            for line in file:
                line = line.split(self.splitter)
                if line[0] != "TABLE" or "TSC-database=validated":
                    self.valid = False
                    return False
        self.valid = True
        for value in self.values:
            if value[3] == "INT":
                if _is_int(value[2]) == True:
                    self.valid = False
                    return False
                if _is_int(value[2]) == True:
                    self.valid = False
                    return False
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
                        _value = e.encrypt(string=value[2], passphrase=self.passphrase)
                        file.write(f"TABLE{self.splitter}{table}{self.splitter}VALUE{self.splitter}{key}{self.splitter}{_value}{self.splitter}{value[3]}\n")
                    else:
                        file.write(f"TABLE{self.splitter}{value[0]}{self.splitter}VALUE{self.splitter}{value[1]}{self.splitter}{value[2]}{self.splitter}{value[3]}\n")
        else:
            print("ERROR")
            print("INVALID DATABASE")
            print("VERIFY DATABASE WITH conn.verify()")

    def read(self, sellectedValue=None, table=None):
        returnedValues = []
        if table == None and sellectedValue == None:
            return self.values
        elif sellectedValue == None and table != None:
            for value in self.values:
                if value[0] == table:
                    returnedValues = returnedValues + [[value[1],value[2]]]
        elif sellectedValue != None and table == None:
            for value in self.values:
                if value[1] == sellectedValue:
                    returnedValues.append(value[2])
        elif sellectedValue != None and table != None:
            for value in self.values:
                if value[0] == table:
                    if value[1] == sellectedValue:
                        return value[2]
                    else:
                        pass
        return returnedValues

    def reset(self, _encrypt=False):
        self.values = []
        self.tables = []
        self.__init__(self.file, _encrypt=_encrypt)

    def edit(self, table, key, value):
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
            return 1
        print("NOTHING IN DATABASE")

    def get_table_list(self):
        return self.tables
    
    def encrypt_database(self, passphrase):
        if _check_file("TSC/plugins/encrypter.py") == True:
            self.encrypt = True
            self.passphrase = passphrase
            self.reset(_encrypt=True)
            return 0
        else:
            print("ERROR")
            print("encrypter.py not in directory ('TSC/plugins/encrypter.py')")
            return 1