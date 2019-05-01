from copy import deepcopy
from random import shuffle

from math import sqrt

from Individual import Individual
from Population import Population


class Algorithm:
    PARAMS_FILENAME = "./params/param.in"

    def __init__(self, problem):
        self.__problem = problem
        self.__currentBest = None
        self.__fitnessOfRuns = []
        self.__loadParams()

    def run(self):
        population = self.__initPopulation()
        counter = self.__iterations
        while counter > 0:
            counter -= 1
            ranked = population.evaluate()
            if self.__isBestSolution(ranked[0]):
                return ranked[0]
            self.__compareWithCurrentBest(ranked[0])
            newPopulationData = []
            newPopulationData.extend(ranked[:self.__eliteSize])
            for i in range(self.__eliteSize, self.__populationSize, 2):
                parentA = population.selection()
                parentB = population.selection()
                childA, childB = parentA.crossover(parentB, self.__crossoverProbability)
                childA.mutate(self.__mutationProbability)
                childB.mutate(self.__mutationProbability)
                newPopulationData.append(childA)
                newPopulationData.append(childB)
            self.__fitnessOfRuns.append(population.totalFitness())
            population = Population(newPopulationData)
        return self.__currentBest

    def getStatistics(self):
        averageFitness = sum(self.__fitnessOfRuns) / self.__iterations
        fitnessStandardDeviation = sqrt(
            sum([(x - averageFitness) ** 2 for x in self.__fitnessOfRuns]) / len(self.__fitnessOfRuns))
        return {"std_dev": fitnessStandardDeviation,
                "average_fitness": averageFitness,
                "fitness": self.__fitnessOfRuns,
                "iterations": self.__iterations}

    def __compareWithCurrentBest(self, individual):
        if self.__currentBest == None:
            self.__currentBest = individual
            return
        if self.__currentBest.fitness() < individual.fitness():
            self.__currentBest = individual

    def __isBestSolution(self, individual):
        return individual.fitness() == self.__problem.size()

    def __initPopulation(self):
        individuals = []
        for i in range(0, self.__populationSize):
            data = deepcopy(self.__problem.data)
            shuffle(data)
            individuals.append(Individual(data))
        return Population(individuals)

    def __loadParams(self):
        f = open(self.PARAMS_FILENAME, "r")
        self.__mutationProbability = float(f.readline().split("=")[1])
        self.__crossoverProbability = float(f.readline().split("=")[1])
        self.__populationSize = int(f.readline().split("=")[1])
        self.__eliteSize = int(f.readline().split("=")[1])
        self.__iterations = int(f.readline().split("=")[1])
