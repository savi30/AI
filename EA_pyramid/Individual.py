import random


class Individual:
    def __init__(self, data):
        self.__data = data

    def fitness(self):
        length = len(self.__data)
        fitness = length
        for i in range(1, length):
            if self.__data[i].length < self.__data[i - 1].length:
                fitness -= 1
            else:
                if self.__data[i].color == self.__data[i - 1].color:
                    fitness -= 1
        return fitness

    def mutate(self, probability):
        if random.random() > probability:
            return

        mutationX = random.randint(0, len(self.__data) - 1)
        mutationY = random.randint(0, len(self.__data) - 1)
        aux = self.__data[mutationX]
        self.__data[mutationX] = self.__data[mutationY]
        self.__data[mutationY] = aux

    def crossover(self, other, probability):
        if random.random() > probability:
            return self, other

        length = len(self.__data)
        child_a_dna = [None] * length
        child_b_dna = [None] * length
        start = random.randint(0, length)
        end = random.randint(0, length)
        if start > end:
            start, end = end, start

        for i in range(start, end):
            child_a_dna[i] = other.__data[i]
            child_b_dna[i] = self.__data[i]

        i = end
        j = end
        while None in child_a_dna:
            if self.__data[i % length] not in child_a_dna:
                child_a_dna[j % length] = self.__data[i % length]
                j += 1
            i += 1

        i = end
        j = end
        while None in child_b_dna:
            if other.__data[i % length] not in child_b_dna:
                child_b_dna[j % length] = other.__data[i % length]
                j += 1
            i += 1

        return Individual(child_a_dna), Individual(child_b_dna)

    def size(self):
        return len(self.__data)

    def __str__(self):
        result = ""
        for e in self.__data:
            result += e.__str__()
        return result


class Cube:
    def __init__(self, length, color):
        self.length = length
        self.color = color

    def __str__(self):
        return ' {0}{1} '.format(self.length, self.color)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.length == other.length and self.color == other.color
