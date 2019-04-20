from domain.state import Tile, Configuration


class NPuzzle:

    def __init__(self, size):
        if size == 4 or size == 9 or size == 16:
            size = size - 1
            initial = self.__readGrid("./resources/" + size.__str__() + "puzzleInitialConf")
            final = self.__readGrid("./resources/" + size.__str__() + "puzzleFinalConf")
            grid = [[Tile() for j in range(len(initial))] for i in range(len(initial))]
            for i in range(len(initial)):
                for j in range(len(final)):
                    grid[i][j] = Tile(initial[i][j], final[i][j], i, j)
            self.__configuration = Configuration(grid)
        else:
            self.__randomSequence(size)

    def __readGrid(self, filepath):
        file = open(filepath, 'r')
        grid = [[int(val) for val in line.split(" ")] for line in file]
        return grid

    def heurustic(self, state):
        '''
        manhattan distance heuristic
        '''
        manhattanDistance = 0
        for tileRow in state.getTiles():
            for tile in tileRow:
                manhattanDistance += self.__computerManhattanDistance(tile, state.getTileByValue(tile.goalValue))
        return manhattanDistance

    def __computerManhattanDistance(self, tile, goalTile):
        manhattanDistance = 0
        manhattanDistance += abs(tile.positionX - goalTile.positionX)
        manhattanDistance += abs(tile.positionY - goalTile.positionY)
        return manhattanDistance

    def getRoot(self):
        return self.__configuration

    def expand(self, conf):
        return conf.nextConfigurations()

    def __randomSequence(self, size):
        pass
