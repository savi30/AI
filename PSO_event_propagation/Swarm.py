from Particle import Particle
from copy import deepcopy


class Swarm:

    def __init__(self, swarmSize, neighbourhoodLength, length, problem):
        self._v = [Particle(length, problem) for _ in range(swarmSize)]
        self._numberOfParticles = self._v.__len__()
        self._neighbourhoodLength = neighbourhoodLength

    def getNeighbours(self, particle):
        elems = self._v
        differences = []
        for other in elems:
            if other == particle:
                continue
            differences.append([abs(particle.getFitness()-other.getFitness()), other])
        n = sorted(differences, key=lambda diff: diff[0])
        n = [diff[1] for diff in n]
        return n[:self._neighbourhoodLength]

    def getBestNeighbour(self, particle):
        neighbours = self.getNeighbours(particle)
        bestFitness = neighbours[0].getFitness()
        bestNeighbour = neighbours[0]
        for neighbour in neighbours:
            if neighbour.getFitness() < bestFitness:
                bestFitness = neighbour.getFitness()
                bestNeighbour = neighbour
        return bestNeighbour

    def getBestParticles(self):
        elems = self._v
        return sorted(elems, key=lambda elem: elem.getFitness())

    def __getitem__(self, pos):
        return self._v[pos]
