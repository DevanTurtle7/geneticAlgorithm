"""
A testing module for salesman_py
"""
from salesman_dna import *
import globals

def test_salesman_dna_init():
    """
    Tests that the dna class properly creates an offspring
    """
    # Setup
    genome = "Test!"

    # Invoke
    offspring = salesman_dna(genome)

    # Analyze
    assert(offspring.genome == genome)

    print("test_salesman_dna_init passed!") # Prints if the test passes

def test_salesman_dna_fitness_square():
    """
    Tests that the dna is accurately analyzing the fitness of each genome
    """
    # Setup
    genome = [[0, 0], [0, 1],[1, 1],[0, 1]]
    expected_fitness = 4

    # Invoke
    offspring = salesman_dna(genome)

    # Analyze
    assert(offspring.fitness() == expected_fitness)
    print("test_salesman_dna_fitness_square passed!")

def test_salesman_dna_fitness_pentagon():
    """
    Tests that the dna is accurately analyzing the fitness of each genome
    """
    # Setup
    genome = [[0,0], [2, -1], [1, -3], [-1, -3], [-2, -1]]
    expected_fitness = 2 + (4 * (5 ** .5))

    # Invoke
    offspring = salesman_dna(genome)

    # Analyze
    difference = abs(offspring.fitness() - expected_fitness) # Since there is weird float rounding in python, assert that the values are "close enough"
    assert(difference <= 0.01)
    print("test_salesman_dna_fitness_pentagon passed!")

def test_salesman_dna_crossover():
    """
    Tests that the DNA's crossover function is working properly
    """
    # Setup
    # Create 2 offsprings with different genomes
    parent_1 = salesman_dna("00000000")
    parent_2 = salesman_dna("11111111")

    # Invoke
    offspring = parent_1.crossover(parent_2, True) # Call crossover with debug mode on

    # Analyze
    offspring_genome = offspring[0].genome
    offspring_midpoint = offspring[1]
    expected_genome = parent_1.genome[0:offspring_midpoint] + parent_2.genome[offspring_midpoint:len(parent_2.genome)]

    assert(offspring_genome == expected_genome)

    print("test_salesman_dna_crossover passed!")

def run_all_tests():
    """
    Runs all the tests
    """
    test_salesman_dna_init()
    test_salesman_dna_fitness_square()
    test_salesman_dna_fitness_pentagon()
    test_salesman_dna_crossover()

run_all_tests()