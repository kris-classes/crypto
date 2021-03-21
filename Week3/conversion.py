"""
HTCS6702 - Cryptography Semester 1 2021

Week 3 Homework - Kris Pritchard / @krp

Homework: For Week 3 homework you're going to create a small Python program which
solves what you were doing with pen & paper in Week 2.

You don't need to change this file.
"""
from helper_functions import binary

"""
Firstly we need to get familiar with Python's built-in functions for converting between data representations:

int() converts a string into an integer.

hex() converts an integer into a hexadecimal string.

bin() converts an integer into a string of binary characters.

ord() returns the ASCII/Unicode integer for a single character.

chr() converts an integer into the ASCII/Unicode character.

Try these out in a Python console/shell/terminal.
NOTE: You're less likely to remember them if you just copy & paste, so type each line out.
"""

"""
Examples below are provided, your job is to combine some of these examples into a small working program.
"""
# Converts the string '240' into the integer 240
int('240')

# Converts a hexadecimal string into the integer 254.
int('0xFE', base=16)

# Gives an error because the string 'hello' is not a number.
# NOTE: What happens if you delete the try/except code and rerun this file with just int('hello')?
try:
    int('hello')
except ValueError:
    print('Caught and ignoring an exception when trying int("hello")')

# Converts the hexadecimal string '0xFE' into the integer 254.
int('0xFE', base=16)

# Converts the integer 195 into the hex string '0xc3'
hex(195)

# Gives an error because hex() only accepts integers and not strings.
try:
    hex('0xc3')
except TypeError: 
    print('Caught and ignoring an exception when trying hex("0xc3")')

# Converts the integer 205 into the string '0b11001101'
bin(205)

# By default Python doesn't display leading-zeros when printing a binary number.
bin(13)  # Will only display '0b1101'

# Gives an error because bin() only accepts integers and not strings.
try:
    bin('123') 
except TypeError:
    print("Caught and ignoring an exception when trying bin('123')")

# I created a binary() function in helper_functions.py which fixes the above problem.
# If you get an error saying 'name binary is not defined' then type: from helper_functions import binary
binary(13)  # Will display '0b00001101 
 
# Looks up the ASCII code for the character 'X' and returns the corresponding integer 88.
ord('X') 

# Gives an error because the string 'hello' is not a single character
try:
    ord('hello')
except TypeError:
    print("Caught and ignoring an exception when trying to run ord('hello')")

# Converts the integer 72 into the character 'H'
chr(72)

# Gives an error because chr() only accepts integers.
try:
    chr('f')
except TypeError:
    print('Caught and ignoring an exception when trying to run chr("f")')

