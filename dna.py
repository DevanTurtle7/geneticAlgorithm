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
        midpoint = random.randrange(1, len(self.genome)-1) # Must include atleast 1 bit of genetic information from each parent
        new_genome = self.genome[0:midpoint] + mate.genome[midpoint:len(mate.genome)]
        
        offspring = dna(new_genome, self.target)

        if not debug:
            return offspring
        else:
            return offspring, midpoint

    def fitness(self):
        fitness = 0
        for i in range(0, len(self.genome)):
            if self.genome[i] == self.target[i]:
                fitness += 1
        
        return fitness