from dna import *
import globals
import random

POPULATION_SIZE = globals.POPULATION_SIZE

def midpoint(upper_bound, lower_bound):
    """
    Returns the midpoint between 2 numbers

    Parameters:
        upper_bound: The larger of the 2 numbers
        lower_bound: The smaller number
    """
    difference = upper_bound - lower_bound
    mid = lower_bound + int(difference / 2)
    return mid

def find_index(value, array):
    """
    Finds the index where an item can be inserted into an array such that
    the final array is organized from smallest to largest by using binary
    search techniques.

    Note: This function is currently modified to only work with DNA objects,
    as it calls fitness() when comparing elements.

    Parameters:
        value: The value of new element being inserted into the array
        array: The array the element is being inserted into
    """
    # Setup
    found_index = False
    length = len(array) # Save the length of the array
    upper_bound = length - 1
    lower_bound = 0
    index = 0

    # Check for small arrays
    if length == 0:
        return 0
    elif length == 1:
        if array[0].fitness() <= value:
            return 1
        else:
            return 0

    # Loop until the index is found
    while not found_index:
        index = midpoint(upper_bound, lower_bound) # Reset the index as the midpoint between the upper and lower bounds

        if upper_bound == lower_bound:
            if array[index].fitness() < value:
                index += 1
            found_index = True
        elif upper_bound - lower_bound == 1:
            if array[upper_bound].fitness() < value:
                index = upper_bound + 1
                found_index = True
            else:
                if array[lower_bound].fitness() <= value:
                    index = lower_bound + 1
                    found_index = True
                else:
                    index = lower_bound
                    found_index = True
        else:
            if array[index].fitness() > value:
                upper_bound = index-1
            elif array[index].fitness() < value:
                lower_bound = index
            elif array[index].fitness() == value:
                found_index = True
    
    
    return index

def sort_population(population):
    """
    Sorts an array of DNA objects by fitness using binary search techniques
    """
    ordered_population = []
    population_length = len(population)

    for offspring in population:
        offspring_fitness = offspring.fitness()
        index = find_index(offspring_fitness, ordered_population)
        ordered_population.insert(index, offspring)

    return ordered_population

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

def main():
    # Setup
    target = globals.target
    target_length = len(target)
    charset_length = len(globals.charset)
    population = []
    next_generation = []
    first_generation = True
    
    # Create N offspring with random genomes
    for _ in range(0, POPULATION_SIZE):
        random_genome = ""

        for index in range(0, target_length):
            random_index = random.randrange(0, charset_length) # Choose a random character from charset to add to the genome
            random_genome += globals.charset[random_index] # Add the random character to the end of the temporary genome string
        
        offspring = dna(random_genome, target) # Create the dna object
        population.append(offspring) # Add the offspring to the population
    
    # Continue to breed new generations until the optimal genome is found
    optimal_genome_found = False
    count = 0
    GENERATION_CAP = globals.GENERATION_CAP

    while not optimal_genome_found:
        count += 1

        if GENERATION_CAP is not False:
            if count > GENERATION_CAP:
                print("Generation cap was reached")
                break
        
        if not first_generation:
            population = next_generation # Set the current population to the new population
            next_generation = [] # Reset next_generation
        else:
            first_generation = False

        ordered_population = sort_population(population)
        most_fit = ordered_population[len(ordered_population) - 1]

        print("Most fit:",most_fit.genome)

        if most_fit.genome == globals.target:
            optimal_genome_found = True

        MATING_POOL_SIZE = globals.MATING_POOL_SIZE
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

if __name__ == "__main__":
    main()
