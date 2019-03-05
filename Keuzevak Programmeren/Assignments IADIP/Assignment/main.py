#!/usr/bin/python

import sys
import functions
import types

'''
The entry-point of our application.
'''
def main():
    current_version = 'calculator version 0.1'
    # Implement basic functionality
    if input() == 'version':
        print(current_version)
    elif input() == 'help':
        print('hello!')
    elif input() == 'quit':
        sys.exit()
            



        
  
if __name__== "__main__":
    main()
