"""
This file contains the DNA class object for the shakespearean genetic
algorithm.

author: Devan Kavalchek
"""

import random
import globals

shakespearean_settings = globals.shakespearean_settings

class shakespearean_dna():
    def __init__(self, genome, target):
        """
        Runs the first time the object is created

        Parameters:
            genome: The genome of self
            target: The ideal genome. Used to analyze the fitness of self
        """
        assert(len(genome) == len(target)) # Check that the length of the genome and the length of the target are the same

        # Assign self's values to the given variables
        self.genome = genome
        self.target = target


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
        new_genome = self.genome[0:midpoint] + mate.genome[midpoint:len(mate.genome)] # A new genome made from a mix of the 2 genomes
        
        offspring = shakespearean_dna(new_genome, self.target) # A new offspring/child made from the new genome

        # Mutations
        if not debug: # Don't predict if in debug mode for more predictable crossovers
            for i in range(0, len(offspring.genome)):
                mutation_chance = random.random()

                # If the random mutation_chance falls beneath or equal to the mutation rate, mutate the dna
                if mutation_chance <= shakespearean_settings.MUTATION_RATE:
                    # Mutate
                    random_char_index = random.randrange(0, len(globals.charset))
                    offspring.genome = globals.change_string_index(offspring.genome, i, globals.charset[random_char_index]) # Replace the DNA at the current index

        if not debug:
            return offspring
        else:
            # If debug mode is on, return the offspring and the midpoint
            return offspring, midpoint

    def fitness(self):
        """
        This function analyzes the fitness of self and returns
        the fitness score.

        In this case, fitness is analyzed by how many characters
        match the target genome. Higher is better.
        """
        # Initialize variables
        fitness = 0

        for i in range(0, len(self.genome)): # Iterate over every character of the genome
            if self.genome[i] == self.target[i]:
                # If the genome character at index i matches the character at target i, add 1 to the fitness score
                fitness += 1
        
        return fitness