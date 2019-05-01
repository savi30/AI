import random


class Individual:
    def __init__(self, data):
        self.__data = data

    def fitness(self):
        length = len(self.__data)
        fitness = length
        for i in range(1, length):
            if self.__data[i].value < self.__data[i - 1].value:
                fitness -= 1
            else:
                if self.__data[i].color == self.__data[i - 1].color:
                    fitness -= 1
        return fitness

    def mutate(self, probability):
        if random.random() > probability:
            return

        mutationX = random.randint(0, len(self.__data))
        mutationY = random.randint(0, len(self.__data))
        aux = self.__data[mutationX]
        self.__data[mutationX] = self.__data[mutationY]
        self.__data[mutationY] = aux

    def crossover(self, other, probability):
        if random.random() > probability:
            return

        length = len(self.__data)
        childA = [None] * length
        childB = [None] * length
        start = random.randint(0, length)
        end = random.randint(0, length)
        if start > end:
            start, end = end, start

        for i in range(start, end + 1):
            childA[i] = other.__data[i]
            childB[i] = self.__data[i]

        i = end
        j = end
        while None in childA:
            if self.__data[i % length] not in childA:
                childA[j % length] = self.__data[i % length]
                j += 1
            i += 1

        i = end
        j = end
        while None in childB:
            if other.__data[i % length] not in childB:
                childB[j % length] = other.__data[i % length]
                j += 1
            i += 1

        return childA, childB

    def size(self):
        return len(self.__data)


class Cube:
    def __init__(self, length, color):
        self.length = length
        self.color = color
