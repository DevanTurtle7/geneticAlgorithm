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
        half_point = random.randrange(len(self.genome))
        new_genome = mate.genoem[0:half_point] + self.genome[half_point:len(self.genome)]
        
        offspring = dna(new_genome, self.target)

        if not debug:
            return offspring
        else:
            return offspring, half_point

    def fitness(self):
        fitness = 0
        for i in range(0, len(self.genome)):
            if self.genome[i] == self.target[i]:
                fitness += 1
        
        return fitness