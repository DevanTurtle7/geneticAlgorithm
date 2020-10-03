"""
Contains variables, functions and algorithms that are referenced and used acrossed multiple files
in this project.

author: Devan Kavalchek
"""

import random

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

def weighted_element(array):
    """
    Returns a random element from a given array, with a higher percentage to choose
    an element towards the end of the array

    Parameters:
        array: The array to select the element from
    """
    # f(x) = 1 - (2 ^ (-10x))

    random_num = random.random() # Get a random number
    weighted_index_float = 1 - (2 ** (-10 * random_num)) # Input the random number into the weighted function
    weighted_index = int(len(array) * weighted_index_float) # Turn that number (0-1) to an index (the percentage through the array)

    return array[weighted_index] # Return the element at the index

def split(an_array):
    """
    A helper function for mergesort.
    Splits an array in half and returns the two halves

    Parameters:
        an_array: The array being split
    """
    length = len(an_array)

    # Create the evens and odds array
    odds = []
    evens = []

    # Copy all of the values at even indexes into evens
    # Copy all of the values at odd indexes into odds
    for index in range(length):
        if index % 2 == 0:
            evens.append(an_array[index])
        else:
            odds.append(an_array[index])

    # Return evens, odds
    return evens, odds

def merge(left, right):
    """
    A helper function for mergesort.
    Merges two arrays together in a sorted fashion.

    Parameters:
        left: 1 of the two arrays being merged
        right: The other array being merged
    """
    # create the big array - big enough to hold all of the elements in
    # left and right
    left_length = len(left)
    right_length = len(right)
    merged = []

    # need 2 indexes: left, right
    left_index = 0
    right_index = 0

    # as long as both left and right still have elements to copy
    while left_index < left_length and right_index < right_length:
        left_value = left[left_index].fitness()
        right_value = right[right_index].fitness()
        # compare the elements at indexes left and right
        # copy the smaller into big
        # increment the two indexes
        if left_value < right_value:
            merged.append(left[left_index])
            left_index += 1
        else: 
            merged.append(right[right_index])
            right_index += 1
    
    if left_index < left_length:
        # copy all of the lements from left into merged
        for index in range(left_index, left_length):
            merged.append(left[index])
    else:
        # copy all of the elements from right into merged
        while right_index < right_length:
            merged.append(right[right_index])
            right_index += 1

    # return big
    return merged

def merge_sort(an_array):
    """
    A sorting array the sorts by breaking an array down into
    single arrays and reconstructing it while sorting
    the elements.

    Parameters:
        an_array: The array being sorted
    """
    # Base cases
    if len(an_array) == 0:
        return an_array
    elif len(an_array) == 1:
        return an_array
    else:
        left, right = split(an_array)

        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)

        merged = merge(sorted_left, sorted_right)

        return merged