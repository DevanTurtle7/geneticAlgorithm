"""
Contains variables and functions that are referenced and used acrossed multiple files
in this project.

author: Devan Kavalchek
"""

MUTATION_RATE = 0.01
POPULATION_SIZE = 1000
MATING_POOL_SIZE = 500
charset = 'abcdefghijklmnopwrstuvwxyz '
target = "to be or not to be"

def change_string_index(string, index, new_char):
    """
    Makes strings mutable. Replaces a string's character at a given index.

    Parameters:
        string: The string to be changed
        index: The index that is being changed
        new_char: The character that index is being changed to
    """
    # Setup
    length = len(string)
    new_string = ""
    first_half = ""
    second_half = ""

    if index == 0: # If the index is the first character there won't be a first half
        second_half = string[1:length] # Set the second half to every letter except the first letter
    elif index == length - 1: # If the index is the last character there won't be a second half
        first_half = string[0:length-1] # Set the first half to every letter except the last letter
    else:
        first_half = string[0:index] # Set the first half to all the characters before index
        second_half = string[index+1:length] # Set the second half to all the characters after index

    new_string = first_half + new_char + second_half # Create the new string by sandwiching the new character between the first and second halves
    return new_string
