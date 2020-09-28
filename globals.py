"""
Contains variables and functions that are referenced and used acrossed multiple files
in this project.

author: Devan Kavalchek
"""

class algorithm_settings:
    def __init__(self, MUTATION_RATE, POPULATION_SIZE, MATING_POOL_SIZE, generation_cap, target=None):
        self.MUTATION_RATE = MUTATION_RATE
        self.POPULATION_SIZE = POPULATION_SIZE
        self.MATING_POOL_SIZE = MATING_POOL_SIZE # NOTE: POPULATION_SIZE divided by MATING_POOL_SIZE should be an int
        self.generation_cap = generation_cap # The maximum amount of generations. Set to False or an int
        self.target = target

shakespearean_settings = algorithm_settings(0.01, 1000, 500, False, "to be or not to be")
salesman_settings = algorithm_settings(0.01, 1000, 500, 100)

charset = 'abcdefghijklmnopwrstuvwxyz '

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
