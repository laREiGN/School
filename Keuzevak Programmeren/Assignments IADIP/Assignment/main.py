#!/usr/bin/python

import sys
import functions as f
import types

current_version = 'calculator version 0.1'

'''
The entry-point of our application.
'''
def main():
    global current_version
    # Indicates whether or not our application should quit
    function = input()
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


    # Implement basic functionality


if __name__== "__main__":
    main()