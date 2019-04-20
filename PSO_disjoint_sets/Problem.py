class Problem:
    def __init__(self):
        self._A = []
        self._S = []

    def getA(self):
        return self._A

    def getS(self):
        return self._S

    def LoadData(self):
        f = open('in.txt', 'r')

        self._A = [int(s) for s in f.readline().split() if s.isdigit()]

        for i in f:
            s = [int(s) for s in i.split() if s.isdigit()]
            self._S += [s]
