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

    for _ in range(0, POPULATION_SIZE):
        random_genome = ""

        for index in range(0, target_length):
            random_index = random.randrange(0, charset_length)
            random_genome += globals.charset[random_index]
        
        offspring = dna(random_genome, target)
        population.append(offspring)

if __name__ == "__main__":
    main()
