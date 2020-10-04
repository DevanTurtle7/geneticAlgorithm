"""
author: Devan Kavalchek
"""

from shakespearean_dna import *
from salesman_dna import *
import globals
import random
import math

merge_sort = globals.merge_sort
weighted_element = globals.weighted_element

def shakespearean_algorithm():
     # Setup
    shakespearean_settings = globals.shakespearean_settings
    target = shakespearean_settings.target
    target_length = len(target)
    charset_length = len(globals.charset)
    population = []
    next_generation = []
    first_generation = True
    POPULATION_SIZE = shakespearean_settings.POPULATION_SIZE
    
    # Create inital population: N offspring with random genomes
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
        
        # Create a new generation
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

def salesman_algorithm():
    # Setup
    POPULATION_SIZE = salesman_settings.POPULATION_SIZE
    population = []
    next_generation = []
    first_generation = True

    # Initialize the points. In this case, the map is a circle
    radius = 20 # The radius of the circle
    num_points = 20 # The number of points
    points = [] # Initialize the array for all the places
    radians = 2 * math.pi

    # Create all the points
    for x in range(0, num_points):
        percent = x/num_points
        pos = radians * percent
        points.append([math.sin(pos) * radius, math.cos(pos) * radius])

    # Create inital population: N offspring with random genomes
    for _ in range(0, POPULATION_SIZE): # Create N offspring
        possible_points = points.copy() # Make a copy of points so that places can be removed to avoid repeats.
        genome = [] # Initialize the genome

        for _ in range(0, num_points): # Create a random genome for the current offspring
            random_index = random.randrange(0, len(possible_points)) # Pick a random point
            genome.append(possible_points[random_index])
            possible_points.remove(possible_points[random_index]) # Remove the point so it can not be chosen again
        
        offspring = salesman_dna(genome) # Create an offspring with the genome
        population.append(offspring) # Add the offspring to the population

    # Continue to breed new generations until the optimal genome is found
    optimal_genome_found = False
    count = 0
    generation_cap = salesman_settings.generation_cap

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
        most_fit = ordered_population[0] # Lower is better in the salesman problem

        if not generation_cap:
            if salesman_settings.target >= most_fit.fitness():
                optimal_genome_found = True

        print("Most fit:",most_fit.fitness())
        print("Least fit:", ordered_population[len(ordered_population) - 1].fitness())

        # Choose N mates
        MATING_POOL_SIZE = salesman_settings.MATING_POOL_SIZE
        mating_pool = []

        for _ in range(0, MATING_POOL_SIZE):
            random_mate = weighted_element(ordered_population, globals.decreasing_function) # Use the decreasing function since the most fit offspring will be at the beginning of the array
            mating_pool.append(random_mate)
            ordered_population.remove(random_mate) # Remove so they are not chosen twice in a row
        # Create a new generation
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
   #shakespearean_algorithm()
   salesman_algorithm()

if __name__ == "__main__":
    main()
