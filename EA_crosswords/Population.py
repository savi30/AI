from random import randint
from Individ import *


class Population:

    def __init__(self, problem):
        self._noOfInd = 0
        self._listOfInd = []
        self.problem = problem

    def add(self, individ):
        self._listOfInd.append(individ)
        self._noOfInd += 1

    def totalFitness(self):
        s = 0
        for i in self._listOfInd:
            s += i.fitness(self.problem)
        return s

    def selection(self):
        chance = randint(0, self.totalFitness())
        for el in self._listOfInd:
            chance -= el.fitness(self.problem)
            if chance <= 0:
                return el

    def offspring(self):
        x = self.selection()
        y = self.selection()
        child = x.crossover(y)

        p = randint(0, 100)
        if p < 10:
            child.mutate()
        return child

    def evaluate(self):
        for i in self._listOfInd:
            if i.fitness(self.problem) == i.n:
                return i
        return None

    def fit(self, i):
        return i.fitness(self.problem)

    def getFit(self):
        return sorted(self._listOfInd, reverse=True, key=self.fit)
