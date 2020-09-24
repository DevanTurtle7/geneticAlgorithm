from dna import *
import globals
import random

POPULATION_SIZE = 1000

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

if __name__ == "__main__":
    main()
