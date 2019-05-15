import sys
import types
import functions as f

current_version = 'calculator version 0.1'
<<<<<<< HEAD
function = input()
=======
function = None
>>>>>>> 3fe9c205130d7ad227238d26d01218b7904abd3c

'''
The entry-point of our application.
'''

def main():
    global current_version
    global function
<<<<<<< HEAD
=======
    function = ''
    function = input()
>>>>>>> 3fe9c205130d7ad227238d26d01218b7904abd3c
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
<<<<<<< HEAD

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
    



=======
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
>>>>>>> 3fe9c205130d7ad227238d26d01218b7904abd3c

if __name__== "__main__":
    main()