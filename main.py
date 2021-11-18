# ESSENTIAL LANGUAGE PACKAGES
import os

import interpreter
from interpreter import *

# EXTERNAL PACKAGES
import sys

# WRITTEN BY ZXRO 2021
# (C) FLYTLABS 2021 FLYTLABS.DEV
# TWITTER.COM/XOZXRO
######################################
# EROS IS AN OPEN SOURCE PROGRAMMING LANGUAGE
# DEDICATED TO AUTOMATION AND EXPIREMENTAL PROJECTS
######################################

# FIND ARGUMENTS
# args = sys.argv

# DETERMIN IF CALLING A FILE
# not currently used for ease of testing
'''
if os.path.exists(args[1]):
    callingFile = True
else:
    callingFile = False
'''
callingFile = True
# MAIN RUNTIME

os.chdir(os.getcwd())

if callingFile:

    # read lines of file into list
    with open(r'test.es', 'r', encoding='utf-8') as parseFile:
        fileText = [x.strip() for x in parseFile.readlines()]
        parseFile.close()

    # send text to intepreter
    interpretStatus = interpreter.createIntepreterSpace(fileText)
    print(interpretStatus)



