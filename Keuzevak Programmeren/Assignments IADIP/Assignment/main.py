#!/usr/bin/python

import sys
import types
import functions as f

current_version = 'calculator version 0.1'
function = None

'''
The entry-point of our application.
'''

def main():
    global current_version
    global function
    function = ''
    function = input()
    # Indicates whether or not our application should quit
    quit = False
    if function == 'quit':
        quit = True
    elif quit == True:
        return
    elif function == 'version':
        print(current_version)
        main()
    elif function == 'help':
        f.print_functions()
        main()
    else:
        process_line()
        main()

def process_line():
    global function
    tokens = function.split(' ')
    operands = []
    for i in reversed(tokens):
        if f.is_function(i) == True:
            func_name = f.get_function(i)
            if len(operands) >= 2 and (i != 'sqrt' and i != 'bin'):
                res = func_name(operands[0], operands[1])
                print(res)
            elif len(operands) == 1 and (i == 'sqrt' or i == 'bin'):
                res = func_name(operands[0])
                print(res)
            else:
                print('invalid number of operands')
        elif i.isnumeric() == True:
            operands.insert(0, int(i))
        else:
            print('unknown token')

if __name__== "__main__":
    main()