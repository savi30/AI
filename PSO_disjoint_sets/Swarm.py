from copy import deepcopy


class Swarm:

    def __init__(self):
        self.v = []
        self.noOfParticles = 0

    def getBestNeighbourhood(self, poz):

        p1 = None
        p2 = None

        if poz - 1 >= 0:
            p1 = self.v[poz-1]
        if poz + 1 < self.noOfParticles:
            p2 = self.v[poz+1]

        if p1 and p2 != None:
            if p1.fitness >= p2.fitness and p1.fitness > self.v[poz].fitness:
                return p1
            elif p2.fitness >= p1.fitness and p2.fitness > self.v[poz].fitness:
                return p2
            else:
                return self.v[poz]
        else:
            return self.v[poz]

    def getBest(self):

        lista = deepcopy(self.v)
        lista.sort(reverse=True, key=lambda indiv: indiv.fitness)
        lista = lista[:5]

        return lista

