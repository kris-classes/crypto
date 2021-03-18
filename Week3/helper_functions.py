"""
Helper functions for Week 3 Homework

You don't need to change this file.
"""

# Converts an integer into a binary string with leading zeros.
def binary(integer, length=8):
    return format(integer, '#0{}b'.format(length+2))  # Don't worry much about what this line means until later in the course.


# Uses an if/else statement to control the flow of the function, and then an Exception to tell the program to abort.
def password_check(password):
    if len(password) < 8:
        print('Password is too short')
        raise Exception('Please choose a longer password')
    else:
        print('Valid password')


# Defines a function called 'and' which takes two integers, prints their binary equivalent, then prints the result of the binary (bitwise) AND operation.
# NOTE: We can't call this function 'and' because that name is reserved in Python. We also can't call this file and.py for the same reason.
def bitwise_and(integer_a, integer_b):
    print(f'The bitwise AND of {binary(integer_a)} and {binary(integer_b)} is: ')
    result = integer_a & integer_b
    print(f'Result: {binary(result)}')
    return result


# Don't touch this function or your code will break.
def FIX_ME(msg):
    print(msg)
    return 123


if __name__ == '__main__':
    # This code only gets run if you run the following command:
    #       python helper_functions.py
    password_check('password123')  # TODO: What happens if you run password_check('abc') ?

    bitwise_and(13, 65)

