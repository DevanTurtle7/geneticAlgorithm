"""
This file contains the tests for dna.py

author: Devan Kavalchek
"""
from dna import *
import globals

def test_dna_init():
    """
    Tests that the dna class properly creates an offspring
    """
    # Setup
    genome = "This is my genome"

    # Invoke
    offspring = dna(genome, genome)

    # Analyze
    assert(offspring.genome == genome)

    print("test_dna_init passed!") # Prints if the test passess

def test_dna_fitness():
    """
    Tests that the dna is accurately analyzing the function of each genome
    """
    # Setup
    genome = "00c0e000i"
    target = "abcdefghi"

    # Invoke
    offspring = dna(genome, target)

    # Analyze
    assert(offspring.fitness() == 3)

    print("test_dna_fitness passed!") # Prints if the test passes

def test_dna_crossover():
    """
    A test that ensures the DNA's crossover function is working properly
    """
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

    print("test_dna_crossover passed!") # Prints if the test passes

def test_mutation():
    """
    A characterization test that tests that the DNA mutates properly
    """
    # Setup
    old_mutation_rate = globals.MUTATION_RATE # Remember the current mutation rate
    globals.MUTATION_RATE = 1 # Set the mutation rate to 100% so that the function can be predictably tested
    random.seed(1290809) # Set the seed so that the function can be predictably tested
    parent_1 = dna("00000000", "taargeet")
    parent_2 = dna("11111111", "taargeet")
    expected_genome = "eyorkowx"

    # Invoke
    offspring = parent_1.crossover(parent_2) # Call crossover and save the returned offspring

    # Analyze
    assert(offspring.genome == expected_genome)

    globals.MUTATION_RATE = old_mutation_rate # Set the mutation rate back to normal

    print("test_mutation passed!") # Prints if the test passes

def run_all_tests():
    """
    Runs all the tests
    """
    test_dna_init()
    test_dna_fitness()
    test_dna_crossover()
    test_mutation()

run_all_tests()
