"""
This file contains the DNA class object.

author: Devan Kavalchek
"""

import random

class dna():
    def __init__(self, genome, target):
        """
        Runs the first time the object is created
        """
        assert(len(genome) == len(target))

        self.genome = genome
        self.target = target


    def crossover(self, mate, debug=False):
        """
        This function crosses the genomes of this offspring with
        another given offspring and returns a new offspring.
        
        The function picks a random midpoint and takes the genetic information
        from parent 1 before that midpoint and combines it with the genetic
        information of parent 2 after that midpoint. It then makes a new
        offspring from that new genome and returns it.

        Parameters:
            mate: The other offspring being crossed over
            debug: If True, this function returns the midpoint as well as the new offspring. Default set to False.
        """
        midpoint = random.randrange(1, len(self.genome)-1) # A random midpoint. Must include atleast 1 bit of genetic information from each parent
        new_genome = self.genome[0:midpoint] + mate.genome[midpoint:len(mate.genome)] 
        
        offspring = dna(new_genome, self.target)

        if not debug:
            return offspring
        else:
            return offspring, midpoint

    def fitness(self):
        # Initialize variables
        fitness = 0

        for i in range(0, len(self.genome)):
            if self.genome[i] == self.target[i]:
                fitness += 1
        
        return fitness