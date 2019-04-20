class Problem:

    def __init__(self):
        self.p = 0
        self.q = 0
        self.table = []
        self.list = []

    def loadFromFile(self):
        f = open("in.txt", "r")

        self.p = int(f.readline())
        self.q = int(f.readline())

        for i in range (0, self.p):
            line = f.readline()
            line = line.strip('\n').split(' ')
            self.table.append(line)

        self.makeList()

    def makeList(self):
        cuv = []
        for i in range(0, self.p):
            for j in range(0, self.q):
                if int(self.table[i][j]) == 0:
                    cuv.append((i, j))
                if len(cuv) > 1 and j+1 >= self.q:
                    self.list.append(cuv)
                    cuv = []
            cuv = []
        cuv = []
        for j in range(0, self.q):
            for i in range(0, self.p):
                if int(self.table[i][j]) == 0:
                    cuv.append((i, j))
                if len(cuv) > 1 and i+1 >= self.p:
                    self.list.append(cuv)
                    cuv = []
            cuv = []
