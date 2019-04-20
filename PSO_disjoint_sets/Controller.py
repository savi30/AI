from Swarm import *
from Problem import *
from Particle import *
from random import randint


class Controller:

    def __init__(self):
        self.swarm = Swarm()
        self.problem = Problem()

    def loadParameters(self):
        self.problem.LoadData()
        for i in range(0, 50):
            self.swarm.v.append(Particle(self.problem))
            for k in range(0, len(self.problem.getA())):
                self.swarm.v[i].data.append(randint(0, 1))
                self.swarm.v[i].velocity.append(0)
            self.swarm.v[i].evaluate()
            self.swarm.noOfParticles += 1

    def iterate(self):
        gBest = self.swarm.getBest()[0]
        for i in range(0, self.swarm.noOfParticles):
            lBest = self.swarm.getBestNeighbourhood(i)
            self.swarm.v[i].bestPosition = gBest.data
            self.swarm.v[i].update(lBest)

    def run(self):

        for i in range(0, 100):
            self.iterate()

        print(self.swarm.getBest()[0].data)
