from dna import *
import globals
import random

POPULATION_SIZE = globals.POPULATION_SIZE

def sort_population(population):
    ordered_population = []
    population_length = len(population)

    # Create a list of all offspring ordered by their fitness
    for i in range(0, population_length):
        offspring = population[i]
        offspring_fitness = offspring.fitness()
                
        if i == 0:
            ordered_population.append(population[i])
        elif i == 1:
            if ordered_population[0].fitness() >= offspring_fitness:
                ordered_population.insert(0, offspring)
            else:
                ordered_population.append(offspring)
        else:
            found_index = False
            index = int(len(ordered_population)/2)

            while not found_index:
                if index < 0 or index >= len(ordered_population):
                    print("error")
                    break
                elif index == 0:
                    if ordered_population[index + 1].fitness() >= offspring_fitness:
                        found_index = True
                    else:
                        index += 1
                elif index == len(ordered_population) - 1:
                    if ordered_population[index - 1].fitness() <= offspring_fitness:
                        found_index = True
                        index += 1
                    else:
                        index -= 1
                else:
                    if ordered_population[index].fitness() <= offspring_fitness:
                        if ordered_population[index + 1].fitness() >= offspring_fitness:
                            index += 1
                            found_index = True
                        else:
                            index += 1
                    else:
                        if ordered_population[index - 1].fitness() <= offspring_fitness:
                            found_index = True
                            index -= 1
                        else:
                            index -= 1

            ordered_population.insert(index, offspring)
    
    return ordered_population

def find_index(value, array):
    # Use a while loop or something
    pass

def sort_population_wip(population):
    """
    Sorts an array of DNA objects by fitness using binary search techniques
    """
    ordered_population = []
    population_length = len(population)

    for offspring in population:
        if len(ordered_population) >= 3:
            for x in range(1, len(ordered_population), 1):
                if ordered_population[x-1].fitness() > ordered_population[x].fitness():
                    print("ERRRRORRR!!! PRINTINTG ARRAY:")
                    for offspring in ordered_population:
                        print(offspring.fitness())
                    raise "ERROR!"

        print("NEW OFFSPRING")
        print()
        offspring_fitness = offspring.fitness()
        print("The fitness is", offspring_fitness)
        index = find_index(offspring_fitness, ordered_population)
        ordered_population.insert(index, offspring)
    
    print("ARRAY:")
    for offspring in ordered_population:
        print(offspring.fitness())

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
    # Create an initial population

    # Setup
    target = globals.target
    target_length = len(target)
    charset_length = len(globals.charset)
    population = []
    
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

    while not optimal_genome_found:
        optimal_genome_found = True

        ordered_population = sort_population(population)
        MATING_POOL_SIZE = globals.MATING_POOL_SIZE
        mating_pool = []

        # Choose N mates
        for i in range(0, MATING_POOL_SIZE):
            random_mate = weighted_element(ordered_population)
            mating_pool.append(random_mate)
            ordered_population.remove(random_mate) # Remove so they are not chosen twice in a row

        """
        for offspring in ordered_population:
            print(offspring.fitness())
        """

if __name__ == "__main__":
    main()
