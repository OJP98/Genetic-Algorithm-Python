import numpy as np
from pprint import pprint
from random import random, choices, uniform, randint, randrange
from typing import List, Callable, Tuple

Phenotype = Tuple[float, float, float]
Population = List[Phenotype]
MAX_VAL = 30


def GeneratePhenotype(max_range: int) -> Phenotype:
    return [uniform(0, max_range), uniform(0, max_range), uniform(0, MAX_VAL)]


def GeneratePopulation(size: int, max_genome_range: int) -> Population:
    return [GeneratePhenotype(max_genome_range) for _ in range(size)]


def CrossOver(a: Phenotype, b: Phenotype) -> Phenotype:
    rand = randint(0, 1)
    fitness = a[2] if rand == 1 else b[2]
    return [a[0], b[1], fitness]


def Mutate(phenotype: Phenotype, num: int = 1, prob: float = 0.5) -> Phenotype:
    for _ in range(num):

        if random() < prob:
            phenotype[0] = phenotype[0] + uniform(1, MAX_VAL)

        if random() < prob:
            phenotype[1] = phenotype[1] + uniform(1, MAX_VAL)

    return phenotype


def SortPopulation(population: Population) -> Population:
    return sorted(population, key=lambda x: x[2], reverse=True)


def Fitness(phenotype: Phenotype):
    pass


if __name__ == '__main__':

    population = GeneratePopulation(10, 10)
    pprint(population)
    print('='*20)
    pprint(SortPopulation(population))
