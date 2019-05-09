from copy import deepcopy

from numpy.random import random


class Particle:

    def __init__(self, length, problem):
        self._position = [0 if random() > 0.5 else 1 for _ in range(length)]
        self._velocity = [0 for _ in range(length)]
        self._problem = problem
        self._fitness = self.evaluate()
        self._bestPosition = deepcopy(self._position)
        self._bestFitness = deepcopy(self._fitness)

    def evaluate(self):
        notifiedMembers = []
        for x in range(self._position.__len__()):
            if self._position[x] == 1:
                notifiedMembers.append(x)
        notifMem = deepcopy(notifiedMembers)
        toBeNotified = set()
        visited = set()
        conn = set()
        visits = 0
        while notifiedMembers.__len__() != 0:
            for member in notifiedMembers:
                for x in range(self._position.__len__()):
                    if x in self._problem.getConnections()[member]:
                        conn = conn | {x}
                toBeNotified = toBeNotified | conn - visited
                visited = visited | {member}
            visits += 1
            notifiedMembers = toBeNotified - visited
        return abs(visits - self._problem.getTime()) + notifMem.__len__()

    def getPosition(self):
        return self._position

    def setVelocity(self,vel):
        self._velocity = vel

    def update(self, pos):
        self._position = deepcopy(pos)
        self._fitness = self.evaluate()
        if self._fitness < self._bestFitness:
            self._bestFitness = deepcopy(self._fitness)
            self._bestPosition = deepcopy(self._position)

    def getFitness(self):
        return self._fitness

    def getBestFitness(self):
        return self._bestFitness

    def getBestPosition(self):
        return self._bestPosition

    def getVelocity(self):
        return self._velocity

    def __str__(self):
        return self._position.__str__()
