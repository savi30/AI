from Individual import Cube


class Pyramid:
    FILENAME = "./data/data01.txt"

    def __init__(self):
        self.data = self.__loadData()

    def __loadData(self):
        f = open(self.FILENAME, "r")

        data = f.readline().split(" ")
        numbers = map(lambda x: x[0], data)
        colors = map(lambda x: x[1], data)
        data = []
        for number, color in zip(numbers, colors):
            data.append(Cube(number, color))
        return data

    def size(self):
        return len(self.data)
