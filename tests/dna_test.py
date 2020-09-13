"""
This file contains the tests for dna.py

author: Devan Kavalchek
"""
from dna import *

def test_dna_init():
    # Setup
    genome = "This is my genome"

    # Invoke
    offspring = dna(genome, genome)

    # Analyze
    assert(offspring.genome == genome)

    print("test_dna_init passed!") # Prints if the test passess

def test_dna_fitness():
    # Setup
    genome = "00c0e000i"
    target = "abcdefghi"

    # Invoke
    offspring = dna(genome, target)

    # Analyze
    assert(offspring.fitness() == 3)

    print("test_dna_fitness passed!") # Prints if the test passes

def test_dna_crossover():
    pass

def run_all_tests():
    test_dna_init()
    test_dna_fitness()

run_all_tests()