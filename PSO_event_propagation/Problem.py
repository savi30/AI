

class Problem:
    def __init__(self):
        self._length = 0
        self._connections = []
        self._time = 0
        self._filename = 'members.in'
        self.loadProblem()

    def loadProblem(self):
        file = open(self._filename, 'r')
        self._time = int(file.readline())
        self._length = int(file.readline())
        for _ in range(self._length):
            mem = file.readline().split(" ")
            rel = []
            for i in range(1, len(mem)):
                rel.append(int(mem[i]))
            self._connections.append(rel)
        file.close()

    def getTime(self):
        return self._time

    def getLength(self):
        return self._length

    def getConnections(self):
        return self._connections
