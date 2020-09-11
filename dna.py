"""
This file contains the DNA class object.

author: Devan Kavalchek
"""

class dna():
    def __init__(self, genome, target):
        """
        Runs the first time the object is created
        """
        assert(len(genome) == len(target))

        self.genome = genome
        self.target = target


    def crossover(self):
        pass

    def fitness(self):
        fitness = 0
        for i in range(0, len(self.genome)):
            if self.genome[i] == self.target[i]:
                fitness += 1
        
        return fitness