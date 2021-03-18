"""
Fix the line that says TODO:

Hint: Use string_with_spaces.py for help.
"""
from helper_functions import FIX_ME


def str_to_ascii_codes(input_string):
    for character in input_string:
        # TODO: Replace FIX_ME with the correct function name from above.
        ascii_code = FIX_ME('TODO: Convert this character into an ascii code') 
        print(f'{ascii_code} ', end='')
    print('')


if __name__ == '__main__':
    str_to_ascii_codes('hello')  # This should print the line '104 101 108 108 111'

