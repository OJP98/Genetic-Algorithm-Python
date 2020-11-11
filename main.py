from pprint import pprint
from random import choices, randint, random, randrange, uniform
from typing import Callable, List, Tuple

import numpy as np

Phenotype = Tuple[float, float, float]
Population = List[Phenotype]
MAX_VAL = 30
MAX_GENERATIONS = 1


def GeneratePhenotype(max_range: int) -> Phenotype:
    return [uniform(0, max_range), uniform(0, max_range), uniform(0, MAX_VAL)]


def GeneratePopulation(size: int, max_genome_range: int) -> Population:
    return [GeneratePhenotype(max_genome_range) for _ in range(size)]


def CrossOver(a: Phenotype, b: Phenotype) -> Tuple[Phenotype, Phenotype]:
    fitness1 = a[2] if randint(0, 1) == 1 else b[2]
    fitness2 = a[2] if randint(0, 1) == 1 else b[2]

    child1 = [a[0], b[1], fitness1]
    child2 = [b[0], a[1], fitness2]
    return [child1, child2]


def Mutate(phenotype: Phenotype, num: int = 1, prob: float = 0.5) -> Phenotype:
    for _ in range(num):

        if random() < prob:
            phenotype[0] = phenotype[0] + uniform(1, MAX_VAL)

        if random() < prob:
            phenotype[1] = phenotype[1] + uniform(1, MAX_VAL)

    return phenotype


def SortPopulation(population: Population) -> Population:
    return sorted(population, key=lambda x: x[2], reverse=True)


def FilterPopulation(population: Population) -> Population:
    return [phenotype for phenotype in population if phenotype[2] > 0]


def Fitness(phenotype: Phenotype):
    pass


if __name__ == '__main__':

    population = GeneratePopulation(size=4, max_genome_range=10)
    pprint(population)

    print('='*30)

    for _ in range(MAX_GENERATIONS):
        # Filter out those who have a fitness value of 0
        filteredPopulation = FilterPopulation(population)

        # Select the best phenotypes based on the fitness value
        sortedPopulation = SortPopulation(population)
        # TODO: Get x% of the sorted population

        nextGen = []

        for i in range(0, len(sortedPopulation), 2):
            child1, child2 = CrossOver(
                sortedPopulation[i], sortedPopulation[i + 1])
            child1 = Mutate(child1)
            child2 = Mutate(child2)
            nextGen += [child1, child2]

        population = nextGen

        pprint(population)
