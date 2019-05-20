'''This file contains small utility functions for working in the python interpreter at the command line'''
'''Included functions are:
        -clear()    -This function acts to clear the console by shifting the command prompt to the top of the page using os.system
                    -Works independent of operating system
        -wipe()     -This prints out 10 new lines to create a gap between old commands and output for easier parsing of new commands and outputs.
                    -Can be adjusted to increase the number of lines printed.
        -reload()   -this function reloads modules which are being edited while the python interpreter is running, without needing to quit() python and import everything again.
                    -takes function=None as a default but can be modified to reload a specific function from the input module
'''

import os
import platform
import importlib



def clear():

    opSys = platform.system()

    if opSys.lower() == 'windows':
        return os.system('cls')
    elif opSys.lower() =='darwin':
        return os.system('clear')
    else:
        print("\nUnkown operating system!\n")

def wipe(nLines = 25):
    print("\n"*nLines)


def reload(module, fn=None):

    if fn != None:
        modFunc = (module, fn)
        flipper = '.'.join(modFunc)
        return importlib.reload(flipper)
    else:
        return importlib.reload(module)


#TODO: create a utility function that prints the x.prettify() of all children of a bsObject with "\n"*5 gaps between each child


    
