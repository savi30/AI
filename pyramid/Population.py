import random


class Population:
    def __init__(self, individuals, problem):
        self.__individuals = individuals
        self.__problem = problem

    def add(self, individual):
        self.__individuals.append(individual)

    def evaluate(self):
        return sorted(self.__individuals, key=lambda x: x.fitness(), reverse=True)[0]

    def selection(self):
        chance = random.randint(0, self.totalFitness())
        for x in self.__individuals:
            chance -= x.fitness()
            if chance <= 0:
                return x

    def totalFitness(self):
        return sum(map(lambda x: x.fitnesS(), self.__individuals))
