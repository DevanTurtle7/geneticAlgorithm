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
    # Setup
    # Create 2 offsprings with different genomes
    parent_1 = dna("00000000", "taargeet")
    parent_2 = dna("11111111", "taargeet")

    # Invoke
    offspring = parent_1.crossover(parent_2, True) # Call crossover with debug mode on

    # Analyze
    offspring_genome = offspring[0].genome
    offspring_midpoint = offspring[1]
    expected_genome = parent_1.genome[0:offspring_midpoint] + parent_2.genome[offspring_midpoint:len(parent_2.genome)]

    assert(offspring_genome == expected_genome)

    print("test_dna_crossover passed!")

def run_all_tests():
    """
    Runs all the tests
    """
    test_dna_init()
    test_dna_fitness()
    test_dna_crossover()

run_all_tests()