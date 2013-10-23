from ADT import State  # , SearchNode, SearchQueue, SearchQueue, SearchProblem
from random import random, randint
from pprint import pprint, pformat


class Grid(State):

    __static_grid = []

    def __init__(self):
        self.grid = Grid.gen_grid()
        self.side = len(self.grid)

    def __str__(self):
        return pformat(self.grid)

    @staticmethod
    def gen_grid(save=True):
        side = randint(4, 8)
        print 'Generating random grid of size %d' % side
        grid = [[random() for _ in xrange(side)] for _ in xrange(side)]

        def mapping(x):
            if x < 0.2:
                return 'R'
            elif x < 0.5:
                return 'X'
            else:
                return '_'
        grid = [[mapping(cell) for cell in row] for row in grid]
        if save:
            Grid.__static_grid = grid
        return grid

g = Grid()
print g
