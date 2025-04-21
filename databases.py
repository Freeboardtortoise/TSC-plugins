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

class Connection:
    def __init__(self, filename):
        self.file = filename
        self.valid = False
        self.splitter = "$|$"
        self.values = []
        self.tables = []
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
                        self.tables.append(line[2])
                    if line[2] == "VALUE":
                        if line[3] == "STRING":
                            self.values.append([line[1], line[3], line[4]])
                        elif line[3] == "INT":
                            value4 = _intify(line[4])
                            if value4 == None:
                                print("ERROR")
                                print("INCORRECT DATATYPE")
                            else:
                                self.values.append([line[1], line[3], value4])
                        elif line[3] == "FLOAT":
                            value4 = _floatify(line[4])
                            if value4 == None:
                                print("ERROR")
                                print("INCORRECT DATATYPE")
                            else:
                                self.values.append([line[1], line[3], value4])

                if line[0] == "TSC-database=validated":
                    self.valid = True

    def make_table(self, name):
        if name in self.tables:
            print("ERROR")
            print(f"TABLE: {name} already exists")
            import sys
            sys.exit(1)
        else:
            self.tables = self.tables + [name]
            return 0

    def clear(self):
        open(self.file, "w").close()

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
                    file.write(f"TABLE{self.splitter}NEW{self.splitter}{table}\n")
                for value in self.values:
                    file.write(f"TABLE{self.splitter}{value[0]}{self.splitter}VALUE{self.splitter}{value[1]}{self.splitter}{value[2]}{self.splitter}{value[3]}\n")
        else:
            print("ERROR")
            print("INVALID DATABASE")
            print("VERIFY DATABASE WITH conn.verify()")

    def read(self, sellectedValue='', table=''):
        returnedValues = []
        if table == '' and sellectedValue == '':
            return self.values
        elif sellectedValue == '' and table != '':
            for value in self.values:
                if value[0] == table:
                    returnedValues = returnedValues + [[value[1],value[2]]]
        elif sellectedValue != '' and table == '':
            for value in self.values:
                if value[1] == sellectedValue:
                    returnedValues.append(value[2])
        elif sellectedValue != '' and table != '':
            for value in self.values:
                if value[0] == table:
                    if value[1] == sellectedValue:
                        return value[2]
                    else:
                        pass
        return returnedValues

    def reset(self):
        self.values = []
        self.tables = []
        self.__init__(self.file)

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