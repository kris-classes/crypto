"""
Takes a string and prints it with spaces in between each character.

You don't need to change this file.
"""

# Breaks a string into individual characters and prints them one at a time.
def str_to_spaces(input_string):
    for character in input_string:
        print(f'{character} ', end='')  # The extra space is needed. end='' stops print() from making a new line for each character.
    print('')  # Print an empty line after the loop. What happens if we delete this part? What happens if we remove , end='' above?


if __name__ == '__main__':
    str_to_spaces('hello')  # Displays the string 'h e l l o'

