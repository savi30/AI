from problem.NPuzzle import NPuzzle
from utils.func_timer import func_timer


class Controller:
    def __init__(self, puzzle):
        self.__problem = NPuzzle(puzzle)

    @func_timer
    def solve_n_puzzle_bfs(self):
        q = [self.__problem.getRoot()]
        while len(q) > 0:
            currentState = q.pop(0)
            if currentState.isSolution():
                return currentState
            q.extend(self.__problem.expand(currentState))

    @func_timer
    def solve_n_puzzle_gbfs(self):
        visited = []
        count = 0
        toVisit = [self.__problem.getRoot()]
        while len(toVisit) > 0:
            currentState = toVisit.pop(0)
            count += 1
            visited.append(currentState)
            if currentState.isSolution():
                print(count)
                return currentState
            aux = []
            for x in self.__problem.expand(currentState):
                if x not in visited:
                    aux.append(x)
            aux = [[x, self.__problem.heurustic(x)] for x in aux]
            aux.sort(key=lambda elem: elem[1])
            aux = [x[0] for x in aux]
            toVisit.extend(aux)
