import main
from dna import *

def test_sort_population():
    # Setup
    genomes = ["hujlo", "hallo",  "aslla", "safea"]
    target = "hello"
    population = []
    
    # Create a sample population
    for i in range(0, 4):
        offspring = dna(genomes[i], target)
        population.append(offspring)

    # Invoke
    result = main.sort_population(population)

    assert(result[0].genome == genomes[3])
    assert(result[1].genome == genomes[2])
    assert(result[2].genome == genomes[0])
    assert(result[3].genome == genomes[1])

    print("test_sort_population passed!")

def test_weighted_element():
    pass


def run_all_tests():
    test_sort_population()

run_all_tests()