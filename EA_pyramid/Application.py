import matplotlib.pyplot as plt

from Algorithm import Algorithm
from Pyramid import Pyramid


def main():
    problem = Pyramid()
    algorithm = Algorithm(problem)
    solution = algorithm.run()
    statistics = algorithm.getStatistics()
    print(solution)

    '''plot stuff(evil laughter)'''
    avg_fitness = statistics["average_fitness"]
    fitness_std_dev = statistics["std_dev"]
    iterations = statistics["iterations"]
    fitness = statistics["fitness"]
    for i in range(len(fitness), iterations):
        fitness.append(None)
    print("Avg fitness: ", avg_fitness)
    print("Fitness standard deviation : ", fitness_std_dev)

    plt.plot(range(iterations), fitness, label="fitness / runs")

    plt.xlabel('Iterations')
    plt.ylabel('Fitness')
    plt.title("Fitness evolution")
    plt.legend()
    plt.show()


main()
