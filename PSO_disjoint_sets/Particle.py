from random import randint


class Particle:

    def __init__(self, problem):
        self.problem = problem
        self.data = []
        self.velocity = []
        self.fitness = 0
        self.bestPosition = []

    @staticmethod
    def is_in(l1, l2):
        cnt = 0
        for i in l1:
            if i in l2:
                cnt += 1

        return cnt == len(l1)

    def evaluate(self):
        cnt = 0

        aux1 = []
        for i in range(len(self.data)):
            if self.data[i] == 1:
                aux1.append(self.problem.getA()[i])

        aux2 = []
        for i in range(len(self.data)):
            if self.data[i] == 0:
                aux2.append(self.problem.getA()[i])

        for s in self.problem.getS():
            if (not self.is_in(s, aux1)) and (not self.is_in(s, aux2)):
                cnt += 1

        self.fitness = cnt

    def update(self, particle):
        for i in range(0, len(self.data)):
            self.velocity[i] = 2 * randint(0, 1) * particle.data[i] + 2 * randint(0, 1) * self.bestPosition[i]
            self.data[i] = (self.data[i] + self.velocity[i]) % 2
