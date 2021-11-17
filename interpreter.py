import functions


def file(readFile):

    createIntepreterSpace(readFile)
    return 'Success interpreting file.'
    '''
    try:
        
    except:
        return 'Error'
    '''
def createIntepreterSpace(code):

    varData = functions.init()

    for line in code:
        spceAlert = False
        lineArr = line.split(' ')
        for elem in line:
            if elem == '\'':
                if spceAlert == True:
                    lineArr_ = lineArr[lineArr.index(elem)-1:] + [' '] + lineArr[:lineArr.index(elem)]

                if line[line.index(elem)+1] == ' ':
                    lineArr_ = lineArr[lineArr.index(elem):] + [' '] + lineArr[:lineArr.index(elem)+1]
                    spceAlert = True

                lineArr = lineArr_

        if lineArr[0] == '#':
            continue

        # test for variable creations
        if lineArr[0].lower() == 'dynamic':
            varData = functions.dynamic(varData, line=line.split())

        if lineArr[0].lower() == 'static':
            varData = functions.static(varData, line=line.split())

        if lineArr[0].lower() == 'new':
            if lineArr[1].lower() == 'bool':
                varData = functions.makeBoolean(varData, line=line.split())

            if lineArr[1].lower() == 'int':
                varData = functions.makeInt(varData, line=line.split())

            if lineArr[1].lower() == 'float':
                varData = functions.makeFloat(varData, line=line.split())

            if lineArr[1].lower() == '[]' or lineArr[1].lower() == 'arr':
                varData = functions.makeArray(varData, line=line.split())


        if lineArr[0].lower() == 'print':

            printLst = []

            # check for string concetation
            if '++' in lineArr:
                includeSpaces = True
                plusInd = lineArr.index('++')
                if '\\' not in lineArr[plusInd]:
                    splits = []
                    for string in ' '.join(lineArr[1:]).split('++'):
                        splits.append(string.strip().split(' '))

            else:
                includeSpaces = False
                splits = [lineArr[1:]]


            for lineArr in splits:
                # check if we're type slicing
                if len(lineArr) > 1:
                    if lineArr[1] == ':':


                        returnArr = varData.search(lineArr[0], lineArr[2].lower())
                        printLst.append(' '.join(returnArr))
                        continue
                    else:
                        # printing a generic string here
                        if '\'' or '\"' in lineArr:
                            try:
                                lineArr.remove('\"')
                                lineArr.remove('\'')
                            except:
                                pass

                        printLst.append(' '.join(lineArr))

                else:
                    printLst.append(str(functions.return_(varData, lineArr[0])))

            if includeSpaces == True:
                joiner = ' '
            else:
                joiner = ''
            totalPrint = joiner.join(printLst)
            print(totalPrint)
    return 'Success intepreting file.'



