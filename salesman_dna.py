"""
This file contains the DNA class object for the traveling salesman
genetic algorithm

author: Devan Kavalchek
"""

import random
import globals

salesman_settings = globals.salesman_settings

class salesman_dna():
    def __init__(self, genome):
        """
        Runs the first time the object is created

        Parameters:
            genome: The genetic information of self
            target: The ideal genome. Used to analyze the fitness of self
        """
        # Assign self's values to the given variables
        self.genome = genome
    
    def crossover(self, mate, debug=False):
        """
        This function crosses the genome of self with
        another given offspring and returns a new offspring.
        
        The function picks a random midpoint and takes the genetic information
        from before the midpoint in self's genome and combines it with the genetic
        information of parent 2 after that midpoint. It then makes a new
        offspring from that new genome and returns it.

        Parameters:
            mate: The other offspring being crossed over
            debug: If True, this function returns the midpoint as well as the new offspring. Default set to False.
        """
        midpoint = random.randrange(1, len(self.genome)-1) # A random midpoint. Must include atleast 1 bit of genetic information from each parent
        new_genome = [] # A new genome made from a mix of the 2 genomes

        for index in range(0, midpoint + 1):
            new_genome.append(self.genome[index])

        for dna in mate.genome:
            if not dna in new_genome:
                new_genome.append(dna)
        
        offspring = salesman_dna(new_genome) # A new offspring/child made from the new genome

        # Mutations
        # Mutation works by swapping an index in the genome with another random index in the genome
        if not debug: # Don't predict if in debug mode for more predictable crossovers
            for i in range(0, len(offspring.genome)):
                mutation_chance = random.random()

                # If the random mutation_chance falls beneath or equal to the mutation rate, mutate the dna
                if mutation_chance <= salesman_settings.MUTATION_RATE:
                    # Mutate
                    random_index = random.randrange(0, len(offspring.genome)) # Pick a random element to swap with
                    offspring.genome[i], offspring.genome[random_index] = offspring.genome[random_index], offspring.genome[i] # Swap

        if not debug:
            return offspring
        else:
            # If debug mode is on, return the offspring and the midpoint
            return offspring, midpoint
    
    def fitness(self):
        """
        Analyzes the fitness of self and returns the fitness score.

        In this case, fitness is analyzed by the length of the path.
        Lower is better.
        """
        # Initialize variables
        fitness = 0
        length = len(self.genome)

        for index in range(0, length):
            # Initialize point variables
            point1 = self.genome[index]
            point2 = None

            if index + 1 == length:
                point2 = self.genome[0]
            else:
                point2 = self.genome[index + 1]
            
            # Calculate the distance between points
            rise = point2[1] - point1[1]
            run = point2[0] - point1[0]
            # Pythagorean theorem
            distance = ((rise ** 2) + (run ** 2)) ** .5

            fitness += distance
        
        return fitness