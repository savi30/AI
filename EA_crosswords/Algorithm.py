from Problem import *
from Population import *
from Individ import *
from random import shuffle


class Algorithm:

    def __init__(self):
        self._problem = Problem()
        self._population = Population(self._problem)

    def read(self):
        self._problem.loadFromFile()
        individ = Individ()
        individ.readWords()
        self._population.add(individ)
        for i in range(0, 20):
            shuffle(individ.x)
            self._population.add(individ)

    def iterate(self):
        gasit = False
        newpop = Population(self._problem)
        for i in range(0, 15):
            child = self._population.offspring()
            newpop.add(child)
        lista = self._population.getFit()
        for i in range(0, 5):
            newpop.add(lista[i])

        if newpop.evaluate() != None:
            print(newpop.evaluate().x)
            gasit = True

        self._population = newpop
        return gasit

    def run(self):
        for i in range(0, 200):
            x = self.iterate()
            if x:
                return
        print(self._population.getFit()[1].x)
