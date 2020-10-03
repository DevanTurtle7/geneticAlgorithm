"""
author: Devan Kavalchek
"""

from shakespearean_dna import *
import globals
import random

shakespearean_settings = globals.shakespearean_settings
POPULATION_SIZE = shakespearean_settings.POPULATION_SIZE
merge_sort = globals.merge_sort

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
