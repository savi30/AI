from copy import deepcopy


class Individ:

    def __init__(self):
        self.n = 0
        self.x = []

    def fitness(self, problem):
        cnt = 0
        lista = deepcopy(problem.list)
        for i in range(0, self.n):
            if len(self.x[i][0]) == len(lista[i]):
                for j in range(0, len(self.x[i][0])):
                    cuv = list(self.x[i][0])
                    if isinstance(lista[i][j], tuple) or lista[i][j] == cuv[j]:
                        lista[i][j] = cuv[j]
                        for a in range(0, len(lista)):
                            for b in range(0, len(lista[a])):
                                if lista[a][b] == (i, j):
                                    lista[a][b] = cuv[j]
                    else:
                        if lista[i][j] != cuv[j]:
                            cnt += 1
                            break
            else:
                cnt += 1

        return self.n - cnt

    def crossover(self, individ):
        child = Individ()
        child.n = individ.n
        child.x = individ.x[0:int(self.n / 2)]
        for i in self.x:
            if i not in child.x:
                child.x.append(i)
        return child

    def mutate(self):
        self.x[0], self.x[self.n - 1] = self.x[self.n - 1], self.x[0]

    def readWords(self):
        f = open("words.txt", "r")
        self.n = int(f.readline())
        for i in range(0, self.n):
            line = f.readline()
            line = line.strip('\n').split(' ')
            self.x.append(line)
