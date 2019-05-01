import random


class Population:
    def __init__(self, individuals):
        self.__individuals = individuals

    def add(self, individual):
        self.__individuals.append(individual)

    def evaluate(self):
        return sorted(self.__individuals, key=lambda x: x.fitness(), reverse=True)

    def selection(self):
        chance = random.randint(0, self.totalFitness())
        for x in self.__individuals:
            chance -= x.fitness()
            if chance <= 0:
                return x

    def totalFitness(self):
        return sum(map(lambda x: x.fitness(), self.__individuals))

    def getData(self):
        return self.__individuals
