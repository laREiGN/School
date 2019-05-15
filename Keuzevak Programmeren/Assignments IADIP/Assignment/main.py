import sys
import functions as f
import types

current_version = 'calculator version 0.1'
function = input()

'''
The entry-point of our application.
'''

def main():
    global current_version
    global function
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

def process_line():
    global function
    tokens = function.split(' ')
    func_name = str(tokens[0])
    if f.is_function(func_name) == True:
        f.get_function(func_name)
        if func_name is not 'sqrt' or 'bin' and len(tokens) == 3:
            opperands = int(tokens[1]), int(tokens[2])
            print(opperands)
        elif len(tokens) == 2 and func_name == 'sqrt' or 'bin':
            opperands = int(tokens[1])
            print(opperands)
        else:
            print('invalid operand type')
            main()
    else:
        print('unknown token')
        main()
    




if __name__== "__main__":
    main()