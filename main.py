# -*- coding: utf-8 -*-
"""AlgoritmosGenéticos

# Genetic Algorithm - Python Implementation

Developers:
* Oscar Juárez
* José Cifuentes

Universidad del Valle de Guatemala - 2020
"""

# Librerías utilizadas y tipo de dato implementado
from pprint import pprint
from random import choices, randint, random, randrange, uniform
from typing import List, Tuple

Phenotype = Tuple[float, float, float]
Population = List[Phenotype]

# Métodos generales


def GeneratePhenotype(max_range: int) -> Phenotype:
    return [uniform(0, max_range), uniform(0, max_range), 0]


def GeneratePopulation(size: int, max_genome_range: int) -> Population:
    return [GeneratePhenotype(max_genome_range) for _ in range(size)]


def CrossOver(a: Phenotype, b: Phenotype) -> Tuple[Phenotype, Phenotype]:
    child1 = [a[0], b[1], 0]
    child2 = [b[0], a[1], 0]
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


def FitnessPopulation(population, fenotipoTop, GetZ, ValidarCondiciones):
    nuevoFenotipoTop = fenotipoTop

    for i in range(len(population)):
        population[i], nuevoFenotipoTop = Fitness(
            population[i], nuevoFenotipoTop, GetZ, ValidarCondiciones)

    return population, nuevoFenotipoTop


# ___________________MAIN TASKS EVOLUTION SIMULATION___________________


# TASK 1
def GetZ1(x1: int, x2: int) -> int:
    return 15*x1 + 30*x2 + 4*x1*x2 - 2*x1**2 - 4*x2**2


def ValidarCondiciones1(x1: int, x2: int) -> int:
    contador = 0
    if not (x1 + 2*x2 <= 30):
        contador += 1

    if not (x1 >= 0 and x2 >= 0):
        contador += 1

    return contador


def Fitness(phenotype, fenotipoTop, GetZ, ValidarCondiciones):
    # Revisar condiciones
    if (ValidarCondiciones(phenotype[0], phenotype[1]) > 0):
        # Si no cumplen return 0
        phenotype[2] = 0
        return phenotype, fenotipoTop

    # Generar z
    valorZ = GetZ(phenotype[0], phenotype[1])

    valorZTop = GetZ(fenotipoTop[0], fenotipoTop[1])
    # Regla de 3
    phenotype[2] = (valorZ*100)/valorZTop
    # Actualizar fitnessTop si es necesario
    if (valorZ > valorZTop):
        return phenotype, phenotype

    return phenotype, fenotipoTop


# Configuración
MAX_VAL = 5
MAX_GENERATIONS = 10
population = GeneratePopulation(size=4, max_genome_range=10)
fenotipoTop = population[0]
fenotipoTop[2] = 1


# Simulación de evolución
for _ in range(MAX_GENERATIONS):
    # Fitness
    # print('****************************************')
    population, fenotipoTop = FitnessPopulation(
        population, fenotipoTop, GetZ1, ValidarCondiciones1)
    # print(f'Population {population} \n FenotipoTop {fenotipoTop}')
    # print()

    # Filter out those who have a fitness value of 0
    filteredPopulation = FilterPopulation(population)
    # print(f'Filtered Population {filteredPopulation}')
    # print()

    # Select the best phenotypes based on the fitness value
    sortedPopulation = SortPopulation(filteredPopulation)
    # print(f'Sorted Population {sortedPopulation}')
    # print()

    nextGen = []

    # Let the parents generate a new generation
    for i in range(0, len(sortedPopulation)-1):
        child1, child2 = CrossOver(
            sortedPopulation[i], sortedPopulation[i + 1])
        child1 = Mutate(child1)
        child2 = Mutate(child2)
        nextGen += [child1, child2]

    population = nextGen


# Resultado final
print(f'''
TASK 1:
X1 = {fenotipoTop[0]} 
X2 = {fenotipoTop[1]} 
Y = {GetZ1(fenotipoTop[0],fenotipoTop[1])}
CONDITIONS = {ValidarCondiciones1(fenotipoTop[0],fenotipoTop[1])==0}
''')


# Task 2
def GetZ2(x1: int, x2: int) -> int:
    return 3*x1+5*x2


def ValidarCondiciones2(x1: int, x2: int) -> int:
    contador = 0
    if not (x1 <= 4):
        contador += 1

    if not (2*x2 <= 12):
        contador += 1

    if not (3*x1+2*x2 <= 18):
        contador += 1

    if not (x1 >= 0 and x2 >= 0):
        contador += 1

    return contador


def Fitness(phenotype, fenotipoTop, GetZ, ValidarCondiciones):
    # Revisar condiciones
    if (ValidarCondiciones(phenotype[0], phenotype[1]) > 0):
        # Si no cumplen return 0
        phenotype[2] = 0
        # print(phenotype)
        return phenotype, fenotipoTop

    # Generar z
    valorZ = GetZ(phenotype[0], phenotype[1])

    valorZTop = GetZ(fenotipoTop[0], fenotipoTop[1])
    # Regla de 3
    phenotype[2] = (valorZ*100)/valorZTop
    # Actualizar fitnessTop si es necesario
    if (valorZ > valorZTop):
        #print(f'Se actualiza {phenotype}')
        return phenotype, phenotype

    return phenotype, fenotipoTop


# Configuración
MAX_GENERATIONS = 25
population = GeneratePopulation(size=4, max_genome_range=2)
fenotipoTop = population[0]
fenotipoTop[2] = 1


# Simulación de evolución
for _ in range(MAX_GENERATIONS):
    # Fiteness
    # print('****************************************')
    population, fenotipoTop = FitnessPopulation(
        population, fenotipoTop, GetZ2, ValidarCondiciones2)
    # print(f'Population {population} \n FenotipoTop {fenotipoTop}')
    # print()

    # Filter out those who have a fitness value of 0
    filteredPopulation = FilterPopulation(population)
    # print(f'Filtered Population {filteredPopulation}')
    # print()

    # Select the best phenotypes based on the fitness value
    sortedPopulation = SortPopulation(filteredPopulation)
    # print(f'Sorted Population {sortedPopulation}')
    # print()

    nextGen = []

    for i in range(0, len(sortedPopulation)-1):
        child1, child2 = CrossOver(
            sortedPopulation[i], sortedPopulation[i + 1])
        child1 = Mutate(child1)
        child2 = Mutate(child2)
        nextGen += [child1, child2]

    population = nextGen


# Resultado final:
print(f'''
TASK 2:
X1 = {fenotipoTop[0]} 
X2 = {fenotipoTop[1]} 
Y = {GetZ2(fenotipoTop[0],fenotipoTop[1])}
CONDITIONS = {ValidarCondiciones2(fenotipoTop[0],fenotipoTop[1])==0}
''')


# TASK 3
def GetZ3(x1: int, x2: int) -> int:
    return 5*x1-x1**2+8*x2-2*x2**2


def ValidarCondiciones3(x1: int, x2: int) -> int:
    contador = 0
    if not (3*x1+2*x2 <= 6):
        contador += 1

    if not (x1 >= 0 and x2 >= 0):
        contador += 1

    return contador


def Fitness(phenotype, fenotipoTop, GetZ, ValidarCondiciones):
    # Revisar condiciones
    if (ValidarCondiciones(phenotype[0], phenotype[1]) > 0):
        # Si no cumplen return 0
        phenotype[2] = 0
        # print(phenotype)
        return phenotype, fenotipoTop
    # Generar z
    valorZ = GetZ(phenotype[0], phenotype[1])

    valorZTop = GetZ(fenotipoTop[0], fenotipoTop[1])
    # Regla de 3
    phenotype[2] = (valorZ*100)/valorZTop
    # Actualizar fitnessTop si es necesario
    if (valorZ > valorZTop):
        #print(f'Se actualiza {phenotype}')
        return phenotype, phenotype

    return phenotype, fenotipoTop


# Configuración
MAX_VAL = 1
MAX_GENERATIONS = 5
population = GeneratePopulation(size=4, max_genome_range=1)
fenotipoTop = population[0]
fenotipoTop[2] = 1


# Simulación de evolución
for _ in range(MAX_GENERATIONS):
    # Fiteness
    # print('****************************************')
    population, fenotipoTop = FitnessPopulation(
        population, fenotipoTop, GetZ3, ValidarCondiciones3)
    #print(f'Population {population} \n FenotipoTop {fenotipoTop}')
    # print()

    # Filter out those who have a fitness value of 0
    filteredPopulation = FilterPopulation(population)
    #print(f'Filtered Population {filteredPopulation}')
    # print()

    # Select the best phenotypes based on the fitness value
    sortedPopulation = SortPopulation(filteredPopulation)
    #print(f'Sorted Population {sortedPopulation}')
    # print()

    nextGen = []

    for i in range(0, len(sortedPopulation)-1):
        child1, child2 = CrossOver(
            sortedPopulation[i], sortedPopulation[i + 1])
        child1 = Mutate(child1)
        child2 = Mutate(child2)
        nextGen += [child1, child2]

    population = nextGen


# Resultado final:
print(f'''
TASK 3:
X1 = {fenotipoTop[0]} 
X2 = {fenotipoTop[1]} 
Y = {GetZ2(fenotipoTop[0],fenotipoTop[1])}
CONDITIONS = {ValidarCondiciones3(fenotipoTop[0],fenotipoTop[1])==0}
''')
