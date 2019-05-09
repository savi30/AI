from Swarm import Swarm
from numpy.random import random


class Controller:

    def __init__(self, problem):
        self._filename = "param.in"
        self.loadParameters()
        self._population = Swarm(self._populationLength, self._neighbourhoodSize, problem.getLength(), problem)

    def iteration(self, w, c1, c2):
        fit = 0
        for i in range(self._populationLength):
            bestNeighbour = self._population.getBestNeighbour(self._population[i])
            vel = []
            for j in range(len(self._population[i].getVelocity())):
                newVelocity = w * self._population[i].getVelocity()[j]
                newVelocity = newVelocity + c1 * random() * bestNeighbour.getPosition()[j] - self._population[i].getPosition()[j]
                newVelocity = newVelocity + c2 * random() * self._population[i].getBestPosition()[j] - self._population[i].getPosition()[j]
                newVelocity=round(newVelocity)
                vel.append(newVelocity % 2)
            self._population[i].setVelocity(vel)
            newPosition = []
            for j in range(len(self._population[i].getVelocity())):
                newPosition.append((self._population[i].getPosition()[j] + self._population[i].getVelocity()[j]) % 2)
            self._population[i].update(newPosition)
            fit = fit + self._population[i].getBestFitness()
        fit /= self._populationLength
        return fit

    def runAlgo(self):
        fit = []
        for i in range(self._noOfIterations):
            fit.append(self.iteration(self._w / (i + 1), self._c1, self._c2))
        best = 0
        for i in range(self._populationLength):
            if self._population[i].getFitness() < self._population[best].getFitness():
                best = i
        fitnessOptim = self._population[best].getFitness()
        indOptim = self._population[best].getPosition()
        return ((indOptim,fitnessOptim),fit)

    def loadParameters(self):
        f = open(self._filename, 'r')
        self._populationLength = int(f.readline().split("=")[1])
        self._w = float(f.readline().split("=")[1])
        self._c1 = float(f.readline().split("=")[1])
        self._c2 = float(f.readline().split("=")[1])
        self._neighbourhoodSize = int(f.readline().split("=")[1])
        self._noOfIterations = int(f.readline().split("=")[1])
        f.close()

    def getPopulation(self):
        return self._population

    def getPopulationLength(self):
        return self._populationLength

    def getNoIterations(self):
        return self._noOfIterations
