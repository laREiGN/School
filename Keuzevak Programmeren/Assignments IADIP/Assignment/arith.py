import arith_tools

from typing import List
from functools import reduce
from operator import add

'''
Calculates the sum of a and b.

Only supports positive integers.
'''
def sum(a, b):
    r = 0                                     # Result
    c = 0                                     # Carry
    result = []

    length_a = arith_tools.get_number_length(a)     # Get length of number a
    length_b = arith_tools.get_number_length(b)     # Get length of number b
    max_length = max(length_a, length_b)            # Calculate maximum a if a > b, else b
    
    a1 = str(a)
    b1 = str(b)
    a_list = list(a1)
    b_list = list(b1)
    a_list.reverse()
    b_list.reverse()

    while max_length > 0:
        if len(a_list) > 0:
            sum1 = a_list.pop(0)
        else:
            sum1 = 0
        if len(b_list) > 0:
            sum2 = b_list.pop(0)
        else:
            sum2 = 0

        current_step = c + int(sum1) + int(sum2)

        if current_step >= 10:
            c = 1
            current_step = current_step - 10
            max_length = max_length - 1
            result.extend(str(current_step))
        else:
            c = 0
            max_length = max_length - 1
            result.extend(str(current_step))
    if c == 1:
        result.extend(str('1'))
    result.reverse()
    result_int = list(map(int, result))
    try:
        r = int("".join(map(str, result_int)))
    except ValueError:
        pass
    return r

'''
Calculates the subtraction of a and b.

Only supports positive integers.
'''
def sub(a, b):
    r = 0                                           # Result
    c = 0                                           # Borrow
    result = []

    s = 1                                           # Sign is positive
    if b > a:
        s = -1
    elif a > b:
        s = 1

    length_a = arith_tools.get_number_length(a)     # Get length of number a
    length_b = arith_tools.get_number_length(b)     # Get length of number b
    max_length = max(length_a, length_b)            # Calculate maximum a if a > b, else b
    
    a1 = str(a)
    b1 = str(b)
    a_list = list(a1)
    b_list = list(b1)
    a_list.reverse()
    b_list.reverse()
    if s == 1:
        while max_length > 0:
            if len(a_list) > 0:
                sub1 = int(a_list.pop(0))
            else: sub1 = 0
            if len(b_list) > 0:
                sub2 = int(b_list.pop(0))
            else: sub2 = 0

            if c == 1:
                sub1 = sub1 - 1

            if sub2 > sub1:
                sub1 = sub1 + 10
                current_step = sub1 - sub2
                c = 1
                max_length = max_length - 1
                result.extend(str(current_step))
            elif sub2 <= sub1:
                current_step = sub1 - sub2
                c = 0
                result.extend(str(current_step))
                max_length = max_length - 1
    elif s == -1:
        while max_length > 0:
            if len(a_list) > 0:
                sub2 = int(a_list.pop(0))
            else: sub2 = 0
            if len(b_list) > 0:
                sub1 = int(b_list.pop(0))
            else: sub1 = 0
            if c == 1:
                sub1 = sub1 - 1

            if sub2 > sub1:
                sub1 = sub1 + 10
                current_step = sub1 - sub2
                c = 1
                max_length = max_length - 1
                result.extend(str(current_step))
            elif sub2 <= sub1:
                current_step = sub1 - sub2
                c = 0
                result.extend(str(current_step))
                max_length = max_length - 1

    result.reverse()
    result_int = list(map(int, result))
    r = int("".join(map(str, result_int)))

    return r * s                                    # Note the sign

'''
Calculates the multiplication of a and b.

Only supports positive integers.
'''
def multiply(a, b):
    r = 0                                     # Result
    while b > 0:
        r = sum(r, a)
        b = b - 1
    return r

'''
Calculates the division of a and b.

Only supports positive integers.
'''
def divide(a, b):                       
    i = 0
    res = 0                                     # Result
    if b > a:
        i = 0
    while a > res:
        res = sum(res, b)
        i = i + 1
    if res > a:
        i = i - 1

    return i

'''
MANDATORY WEEK 5
'''

'''
Calculates the power of a and b.

Only supports positive integers.
'''
def power(a, b):
    r = 1                                     # Result
    while b > 0:
        r = multiply(r, a)
        b = b - 1
    return r

'''
Calculates the square root of a and b.

Only supports positive integers.
'''
def sqrt(a):
    if a <= 1:                                      # Early escape
        return a

    i = 1                                           # Increments
    r = 1                                           # Result of multiplication with i
    res = 0
    
    while res < a:
        res = power(r,2)
        i = i + 1
        r = r + 1
    if res > a:
        i = i - 1

    return sub(i, 1)                                # Subtract one from increment


'''
Calculates the modulo of a and b.

Only supports positive integers.
'''
def mod(a, b):
    return int(sub(a, multiply(divide(a, b), b)))        # Calculate a - ((a / b) * b)

'''
Calculates the gcd of a and b.

Only supports positive integers.
'''
def gcd(a, b):
    a1 = a
    b1 = b
    res = 1
    b1_list = []
    while res > 0:
        res = mod(a1, b1)
        a1 = b1
        b1 = res
        b1_list.append(res)
    if len(b1_list) == 1:
        return b
    else:
        return int(b1_list[-2])

    
'''
Calculates the lcm of a two integers.

Only supports positive integers.
'''
def lcm(a, b):
    return divide(multiply(a, b), gcd(a, b))
'''
Converts a binary string to a decimal integer.
'''
def bin(a):
    binaryNum = str(a)
    binaryNum = list(binaryNum)
    binaryNum.reverse()
    steps = [1]
    count = 1
    amt = 0

    for i in range (1,len(binaryNum)):
        total = multiply(count, 2)
        count = total
        steps.append(count)
    deep = zip(binaryNum, steps)
    for k, v in deep:
        if k == '1':
            amt += v
    return amt
