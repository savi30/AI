import copy


class Tile:
    def __init__(self, value=None, goalValue=None, x=None, y=None):
        self.value = value
        self.goalValue = goalValue
        self.positionX = x
        self.positionY = y


class Configuration:
    def __init__(self, tiles, prevConf=None):
        self._prevConf = prevConf
        self._tiles = tiles

    def getTileByValue(self, value):
        v = []
        for i in range(len(self._tiles)):
            v.extend(self._tiles[i])
        return list(filter(lambda x: (x.value == value), v))[0]

    def nextConfigurations(self):
        nextConfigs = []
        i, j = self.__getIndicesOfFreeSpace(self._tiles)
        prev_i, prev_j = -1, -1
        if self._prevConf is not None:
            prev_i, prev_j = self.__getIndicesOfFreeSpace(self._prevConf._tiles)
        size = len(self._tiles)

        possibleMoves = []
        if i + 1 < size:
            possibleMoves.append((i + 1, j))
        if i - 1 >= 0:
            possibleMoves.append((i - 1, j))
        if j + 1 < size:
            possibleMoves.append((i, j + 1))
        if j - 1 >= 0:
            possibleMoves.append((i, j - 1))

        possibleMoves = list(filter(lambda x: (x != (prev_i, prev_j)), possibleMoves))

        for move in possibleMoves:
            aux = copy.deepcopy(self._tiles)
            auxVal = aux[move[0]][move[1]].value
            aux[move[0]][move[1]].value = aux[i][j].value
            aux[i][j].value = auxVal
            nextConfigs.append(Configuration(aux, self))

        return nextConfigs

    def __getIndicesOfFreeSpace(self, conf):
        size = len(conf)
        for i in range(size):
            for j in range(size):
                if conf[i][j].value == 0:
                    return i, j

    def isSolution(self):
        for tileRow in self._tiles:
            for tile in tileRow:
                if tile.value != tile.goalValue:
                    return False
        return True

    def getTiles(self):
        return self._tiles

    def __str__(self):
        str = ""
        for tileRow in self._tiles:
            for tile in tileRow:
                str += tile.value.__str__() + " "
            str += "\n"
        return str
