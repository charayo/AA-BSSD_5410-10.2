# Genetic Algorithm
# taken from: https://www.geeksforgeeks.org/genetic-algorithms/#
# on: 03/2/2023
# CHANGELOG
# - turn the individual class to a module


from Individual import *

# Number of individuals in each generation
POPULATION_SIZE = 1500

# generations limit
G_LIMIT = 1000

# Valid genes
GENES = '01'

# Target string to be generated
TARGET = 850


def look_up_table():
    values = [
        360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147,
        78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
        87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,
        312
    ]
    weights = [[
        7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
        42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,
        3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13
    ]]

    d = {i + 1: (values[i], weights[0][i]) for i in range(len(values))}
    return d


LOOKUP_TABLE = look_up_table()


# Driver code
def main():
    global POPULATION_SIZE

    # current generation
    generation = 1

    found = False
    population = []

    # create initial population
    for i in range(POPULATION_SIZE):
        gnome = Individual.create_gnome(len(LOOKUP_TABLE.keys()))
        population.append(Individual(gnome, TARGET, GENES, LOOKUP_TABLE))

    while not found:

        # sort the population in increasing order of fitness score
        population = list(reversed(sorted(population, key=lambda x: x.fitness)))

        # Otherwise generate new offsprings for new generation
        new_generation = []

        # Perform Elitism, that mean 10% of the fittest population
        # goes to the next generation
        s = int((10 * POPULATION_SIZE) / 100)
        new_generation.extend(population[:s])

        # From 50% of the fittest population, Individuals
        # will mate to produce offspring
        s = int((90 * POPULATION_SIZE) / 100)
        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = parent1.mate(parent2)
            new_generation.append(child)

        population = new_generation

        print("Generation: {}\tString: {}\tFitness: {}". \
              format(generation,
                     "".join(population[0].chromosome),
                     population[0].fitness))

        generation += 1
        if generation == G_LIMIT:
            break

    print("Generation: {}\tString: {}\tFitness: {}". \
          format(generation,
                 "".join(population[0].chromosome),
                 population[0].fitness))


if __name__ == '__main__':
    main()
