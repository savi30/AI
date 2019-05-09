import matplotlib.pyplot as plt

from Controller import Controller
from Problem import Problem


class Main:
    def __init__(self):
        self._problem = Problem()
        self._controller = Controller(self._problem)

    def main(self):
        fitness = []

        avg_fitness = 0
        runs = 30
        run = 0
        ind_fitness_list = []
        indOptim = []
        indFit = 0

        while run < runs:
            controller = Controller(self._problem)

            ((indOptim, indFit), fitness) = controller.runAlgo()

            avg_fitness += indFit
            ind_fitness_list.append(indFit)

            run += 1

        avg_fitness /= runs
        fitness_stddev = sum([(x - avg_fitness) ** 2 for x in ind_fitness_list]) / (runs - 1)

        print("Avg. solution fitness:", avg_fitness)
        print("Std. dev. of the solutions' fitness:", fitness_stddev)

        plt.plot(range(self._controller.getNoIterations()), fitness, label='fitness / runs')

        plt.xlabel('iteration')
        plt.ylabel('fitness')
        plt.legend()
        plt.show()

        print("Result should either be [0,1,0,0,0,0] or [0,0,0,0,1,0]")
        print('Result: ', indOptim, "with fitness", indFit)


if __name__ == '__main__':
    main = Main()
    main.main()
