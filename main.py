from dna import *
import globals
import random

POPULATION_SIZE = globals.POPULATION_SIZE

def main():

    # Create an initial population

    # Setup
    target = globals.target
    target_length = len(target)
    charset_length = len(globals.charset)
    population = []
    
    # Create N offspring with random genomes
    for _ in range(0, POPULATION_SIZE):
        random_genome = ""

        for index in range(0, target_length):
            random_index = random.randrange(0, charset_length) # Choose a random character from charset to add to the genome
            random_genome += globals.charset[random_index] # Add the random character to the end of the temporary genome string
        
        offspring = dna(random_genome, target) # Create the dna object
        population.append(offspring) # Add the offspring to the population

    
    # Continue to breed new generations until the optimal genome is found

    optimal_genome_found = False

    while not optimal_genome_found:
        mating_pool = []
        ordered_population = []
        optimal_genome_found = True

        # Create a list of all offspring ordered by their fitness
        for i in range(0, POPULATION_SIZE):
            print(i)
            offspring = population[i]
            offspring_fitness = offspring.fitness()

            if i == 0:
                ordered_population.append(population[i])
            elif i == 1:
                if ordered_population[0].fitness() >= offspring_fitness:
                    ordered_population.insert(0, offspring)
                else:
                    ordered_population.append(offspring)
            else:
                found_index = False
                index = int(len(ordered_population)/2)

                while not found_index:
                    if index < 0 or index >= len(ordered_population):
                        print("error")
                        break
                    elif index == 0:
                        if ordered_population[index + 1].fitness() >= offspring_fitness:
                            found_index = True

                            ordered_population.insert(index, offspring)
                        else:
                            index += 1
                    elif index == len(ordered_population) - 1:
                        if ordered_population[index - 1].fitness() <= offspring_fitness:
                            found_index = True

                            ordered_population.insert(index, offspring)
                        else:
                            index -= 1
                    else:
                        if ordered_population[index].fitness() <= offspring_fitness:
                            if ordered_population[index + 1].fitness() >= offspring_fitness:
                                found_index = True

                                ordered_population.insert(index, offspring)
                            else:
                                index += 1
                        else:
                            if ordered_population[index - 1].fitness() <= offspring_fitness:
                                found_index = True
                                
                                ordered_population.insert(index - 1, offspring)
                            else:
                                index -= 1

    for offspring in ordered_population:
        print(offspring.fitness())

if __name__ == "__main__":
    main()
