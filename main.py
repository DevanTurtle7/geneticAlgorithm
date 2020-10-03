"""
author: Devan Kavalchek
"""

from shakespearean_dna import *
import globals
import random

shakespearean_settings = globals.shakespearean_settings

POPULATION_SIZE = shakespearean_settings.POPULATION_SIZE

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

def shakespearean_algorithm():
     # Setup
    target = shakespearean_settings.target
    target_length = len(target)
    charset_length = len(globals.charset)
    population = []
    next_generation = []
    first_generation = True
    
    # Create N offspring with random genomes
    for _ in range(0, POPULATION_SIZE):
        random_genome = ""

        for _ in range(0, target_length):
            random_index = random.randrange(0, charset_length) # Choose a random character from charset to add to the genome
            random_genome += globals.charset[random_index] # Add the random character to the end of the temporary genome string
        
        offspring = shakespearean_dna(random_genome, target) # Create the dna object
        population.append(offspring) # Add the offspring to the population
    
    # Continue to breed new generations until the optimal genome is found
    optimal_genome_found = False
    count = 0
    generation_cap = shakespearean_settings.generation_cap

    while not optimal_genome_found:
        count += 1

        if generation_cap is not False:
            if count > generation_cap:
                print("Generation cap was reached")
                break
        
        if not first_generation:
            population = next_generation # Set the current population to the new population
            next_generation = [] # Reset next_generation
        else:
            first_generation = False

        ordered_population = merge_sort(population)
        most_fit = ordered_population[len(ordered_population) - 1]

        print("Most fit:",most_fit.genome)

        if most_fit.genome == shakespearean_settings.target:
            optimal_genome_found = True

        MATING_POOL_SIZE = shakespearean_settings.MATING_POOL_SIZE
        mating_pool = []

        # Choose N mates
        for _ in range(0, MATING_POOL_SIZE):
            random_mate = weighted_element(ordered_population)
            mating_pool.append(random_mate)
            ordered_population.remove(random_mate) # Remove so they are not chosen twice in a row
        
        children = POPULATION_SIZE // MATING_POOL_SIZE # How many children each offspring needs to have to repopulate the population

        for mate in mating_pool:
            for _ in range(0, children): # Create the correct number of offspring to repopulate the population
                # Pick a random mate
                random_index = random.randrange(0, len(mating_pool))
                random_mate = mating_pool[random_index]
                
                # Create a new offspring
                offspring = mate.crossover(random_mate)
                next_generation.append(offspring)

    if optimal_genome_found:
        print("Success! It took", count, "generations!")

def main():
   shakespearean_algorithm()

if __name__ == "__main__":
    main()
