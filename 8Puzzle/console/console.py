from controller.controller import Controller


class Console:

    def __init__(self):
        self._controller = Controller(9)

    def run(self):
        running = True
        self.__print_options()
        while running:
            cmd = input(">>")
            try:
                cmd = int(cmd)
            except ValueError:
                print("Invalid command. Type 'help' for help")
                continue
            if cmd == 0:
                exit(0)
            if cmd == 1:
                self.__readPuzzleConf()
            if cmd == 2:
                self._controller.solve_n_puzzle_bfs()
            if cmd == 3:
                self._controller.solve_n_puzzle_gbfs()

    def __readPuzzleConf(self):
        val = input("insert puzzle (default 9) : ")
        try:
            val = int(val)
            if self.__is_perfect_square(val):
                self._controller = Controller(val)
            else:
                raise ValueError("value must be a perfect square")
        except ValueError as e:
            print("invalid value" + e.__str__())
        return 8

    @staticmethod
    def __print_options():
        print("0 - exit")
        print("1 - Choose puzzle size")
        print("2 - Solve with bfs")
        print("3 - Solve with gbfs")

    def __is_perfect_square(self, n):
        x = n // 2
        y = set([x])
        while x * x != n:
            x = (x + (n // x)) // 2
            if x in y: return False
            y.add(x)
        return True
