class var:
    def __init__(self):
        self.dataDict = {}

    def exists(self,name):
        try:
            test = self.dataDict[name]
            return True
        except:
            return False

    def add(self,name,data):
        self.dataDict[name] = ' '.join(data)

    def addBool(self,name,data):
        self.dataDict[name] = data

    def addInt(self,name,data):
        self.dataDict[name] = int(data)

    def addFloat(self,name,data):
        self.dataDict[name] = float(data)

    def addArray(self,name,data):
        self.dataDict[name] = data

    def return_(self,name):
        return self.dataDict[name]

    def search(self, var, type):

        returnList = []

        analyzedStr = self.dataDict[var]

        # check to see if variable is a list
        if isinstance(analyzedStr,list):
            analyzedElem = analyzedStr
        else:
            analyzedElem = analyzedStr.split()

        if type == 'str' or type == 'string':

            for elem in analyzedElem:
                try:
                    int(elem)
                except:
                    try:
                        float(elem)
                    except:
                        if not isinstance(elem,list):
                            returnList.append(elem)

        else:
            for elem in analyzedElem:

                if type == 'arr' or type == '[]':
                    if isinstance(elem, list):
                        returnList.append(elem)
                        continue
                    else:
                        pass

                try:
                    if type == 'int':
                        int(elem)
                        returnList.append(elem)

                except:
                    pass

                try:
                    if type == 'float':
                        float(elem)
                        try:
                            int(elem)
                        except:
                            returnList.append(elem)
                except:
                    pass

        return returnList

def init():
    return var()


# VARIABLE functions
# SET / CHANGE FUNCTIONS
def dynamic(varData, line=[]):

    # setting a DYNAMIC variable
    # first we are going to check for syntax correctness
    if line[2] == '=' or line[2] == 'is':
        syntax = True
    else:
        syntax = False

    if syntax:
        varData.add(line[1],line[3:])

    return varData

def static(varData, line=[]):

    # setting a STATIC variable
    # first we are going to check for syntax correctness
    if line[2] == '=' or line[2] == 'is':
        syntax = True
    else:
        syntax = False

    if syntax:

        if varData.exists(line[3]):

            if len(line) > 4:

                if line[4] == ':':
                    findData = varData.search(line[3],line[5])
                    varData.add(line[1], findData)

            else:
                varData.add(line[1], varData.return_(line[3:]))
        else:
            varData.add(line[1], line[3:])

    return varData


# creating a boolean
# a true or false expression
# new bool name = 'true' 'false' or function / var
# 0   1    2    3 4 ...
def makeBoolean(varData, line=[]):
    if varData.exists(line[4]):
        if varData.return_(line[4]) == 'True' or varData.return_(line[4]) == 'False':
            varData.addBool(line[2], varData.return_(line[4]))
            return varData
        else:
            pass
    varData.addBool(line[2], line[4])
    return varData


# checking for an int
# returning a boolean stating
def makeInt(varData, line=[]):

    # new int seven = 7
    # 0   1   2     3 4

    if varData.exists(line[4]):
        try:
            int(varData.return_(line[4]))
            varData.addInt(line[2], varData.return_(line[4]))
            return varData

        except:
            print('CAST VAR IS NOT AN (INT)')

    try:
        int(line[4])
        varData.addInt(line[2], line[4])
    except:
        print('TYPE ERROR, TYPE IS NOT (INT)')

    return varData



def makeFloat(varData,line=[]):
    # new int seven = 7
    # 0   1   2     3 4

    if varData.exists(line[4]):
        try:
            float(varData.return_(line[4]))
            varData.addFloat(line[2], varData.return_(line[4]))
            return varData

        except:
            print('CAST VAR IS NOT A (FLOAT)')

    try:
        float(line[4])
        varData.addFloat(line[2], line[4])
    except:
        print('TYPE ERROR, TYPE IS NOT A (FLOAT)')

    return varData

def makeArray(varData,line=[]):

    # new [] test = array 
    # 0   1  2    3 4 5 ...

    buildArr = []

    if len(line) < 4:
        # here we are trying to type convert
        splitchar = line[1][1]
        # no character specified so assumes a space
        if splitchar == ']': splitchar = ' '

        # retrieve the data within the variable and split by the specified token
        parseData = varData.return_(line[2][:-1])

        for char in parseData.split(splitchar):
            buildArr.append(char.strip())

        # append the built array into the data dictionary
        varData.addArray(line[2], buildArr)

        return varData

    # allow for [x,y,z] syntax
    if line[4][0] == '[':
        if len(line[4:]) > 1:
            arrStr = str(''.join(line[4:])).replace('[','')
        else:
            arrStr = str(line[4]).replace('[','')
        arrData = arrStr.replace(']','')

        splitchar = ','

        for char in arrData.split(splitchar):
            if varData.exists(char.strip()):
                buildArr.append(varData.return_(char.strip()))
            else:
                buildArr.append(char.strip())

    else:
        typeConv = False
        # here we locate the character which we would like to
        # segment the data into an array by
        # this will be important as this should be customizable with relative ease
        # in order to easily segment more complex data into arrays
        splitchar = line[1][1]
        # no character specified so assumes a space
        if splitchar == ']': splitchar = ' '

        # checks to see if there is only one argument remaining
        if len(line[4:]) > 1 and line[5] != ':':
            arrData = ' '.join(line[4:])
        else:
            arrData = line[4]

            if arrData[-1] == ';':
                # type converting into a new variable
                typeConv = True
                arrData = varData.return_(arrData[:-1])
            else:
                typeConv = False

            try:
                if line[5] == ':':
                    # we are type slicing one variable into a list
                    arrData = varData.search(arrData, line[6])

                    if line[6] == 'arr':
                        typeConv = False
                    else:
                        arrData = ' '.join(arrData)
                        splitchar = ' '
                    typeConv = False
                else:
                    typeConv = False
            except:
                pass



        # iterate through the given data using our specified token
        # strip spaces off incase they were used alongside the token
        if isinstance(arrData,list):
            buildArr = arrData
        else:
            scanData = arrData.split(splitchar)

            for char in scanData:

                if typeConv is False and varData.exists(char.strip()):
                    buildArr.append(varData.return_(char.strip()))
                else:
                    buildArr.append(char.strip())

    # append the built array into the data dictionary
    varData.addArray(line[2], buildArr)

    # return the complete dictionary
    return varData

# VARIABLE RETURN FUNCTION
def return_(varData, var):
    return varData.return_(var)

def search(varData, var, type):
    return varData.search(var,type)




def createVar(self):
    return None
