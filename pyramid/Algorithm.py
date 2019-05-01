from random import shuffle

from Individual import Individual


class Algorithm:
    PARAMS_FILENAME = "./params/param.in"

    def __init__(self, problem):
        self.__problem = problem
        self.__loadParams()

    def run(self):
        population = self.__initPopulation()
        while self.__iterations > 0:
            self.__iterations -= 1

    def __initPopulation(self):
        population = []
        data = self.__problem.data
        for i in range(0, self.__populationSize):
            shuffle(data)
            population.append(Individual(data))
        return population

    def __loadParams(self):
        f = open(self.PARAMS_FILENAME, "r")
        self.__mutationProbability = float(f.readline().split("=")[1])
        self.__crossoverProbability = float(f.readline().split("=")[1])
        self.__populationSize = int(f.readline().split("=")[1])
        self.__iterations = int(f.readline().split("=")[1])
