"""
This file contains the tests for dna.py

author: Devan Kavalchek
"""
from dna import *

def test_dna_init():
    genome = "This is my genome"
    offspring = dna(genome, genome)

    assert(offspring.genome == genome)

    print("test_dna_init passed!") # Prints if the test passess

def test_dna_fitness():
    genome = "00c0e000i"
    target = "abcdefghi"
    offspring = dna(genome, target)

    assert(offspring.fitness() == 3)

    print("test_dna_fitness passed!") # Prints if the test passes

def run_all_tests():
    test_dna_init()
    test_dna_fitness()

run_all_tests()