from ADT import State  # , SearchNode, SearchQueue, SearchQueue, SearchProblem
from random import random, randint
from pprint import pprint, pformat


class Grid(State):

    __static_grid = []

    def __init__(self, restore=False):
        self.grid = Grid.gen_grid() if not restore else Grid.__static_grid
        self.side = len(self.grid)
        self.parts_locations = self.store_part_locations()

    def __str__(self):
        s = pformat(self.grid)
        #s += "\n %s" % pformat(self.parts_locations)
        return s

    def store_part_locations(self):
        locations = []
        for i in xrange(len(self.grid)):
            for j in xrange(len(self.grid[i])):
                if self.grid[i][j] == 'X':
                    locations.append((i, j))
        return locations

    def __eq__(self, other):
        return self.grid == other.grid

    def __ne__(self, other):
        return self.grid != other.grid

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
g2 = Grid(restore=True)
print g == g2
