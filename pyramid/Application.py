from random import shuffle

from Algorithm import Algorithm
from Problem import Problem


def main():
    problem = Problem()
    algorithm = Algorithm(problem)
    statistic = algorithm.run()
    '''plot stuff(evil laughter)'''

main()