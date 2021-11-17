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
        analyzedElem = analyzedStr.split()

        if type == 'int':
            for elem in analyzedElem:
                try:
                    int(elem)
                    returnList.append(elem)
                except:
                    try:
                        int(elem[1:])
                        returnList.append(elem[1:])
                    except:
                        try:
                            int(elem[:-1])
                            returnList.append(elem[:-1])
                        except:
                            try:
                                test = elem[:-1]
                                int(test[1:])
                                returnList.append(int(test[1:]))
                            except:
                                pass
                    pass

        if type == 'str' or type == 'string':

            returnList = []

            analyzedStr = self.dataDict[var]
            analyzedElem = analyzedStr.split()

            for elem in analyzedElem:
                try:
                    int(elem)
                except:
                    returnList.append(elem)

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

    # new [] test = array bullshit
    # 1   2  3    4 5 ...

    buildArr = []

    if line[5:][0] == '[':
        # ill deal with this bvullshit later
        pass
    else:
        for char in line[4:]:
            if varData.exists(char):
                buildArr.append(varData.return_(char))
            else:
                buildArr.append(char)

    varData.addArray(line[2], buildArr)

    return varData

# VARIABLE RETURN FUNCTION
def return_(varData, var):
    return varData.return_(var)

def search(varData, var, type):
    return varData.search(var,type)




def createVar(self):
    return None