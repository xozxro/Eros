# ESSENTIAL LANGUAGE PACKAGES
import os

import interpreter
from interpreter import *

# EXTERNAL PACKAGES
import sys



# WRITTEN BY MICHAEL BENJAMIN 2021
# (C) FLYTLABS 2021 FLYTLABS.DEV
######################################
# FLYTLANG IS AN OPEN SOURCE PROGRAMMING LANGUAGE
# DEDICATED TO AUTOMATION AND EXPIREMENTAL PROJECTS
######################################

# FIND ARGUMENTS
# args = sys.argv

# DETERMIN IF CALLING A FILE
'''
if os.path.exists(args[1]):
    callingFile = True
else:
    callingFile = False
'''
callingFile = True
# MAIN RUNTIME

if callingFile:

    # read lines of file into list
    with open(r'T:\projects\SORTED\eros\test.es', 'r', encoding='utf-8') as parseFile:
        fileText = [x.strip() for x in parseFile.readlines()]
        parseFile.close()

    # send text to intepreter
    interpretStatus = interpreter.createIntepreterSpace(fileText)
    print(interpretStatus)



