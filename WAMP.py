from ADTs import State, SearchNode, SearchProblem#, SearchQueue
from random import random, randint
from pprint import pprint, pformat


class Grid(State):

    __static_grid = []

    def __init__(self, restore=False, save=True):
        self.grid = Grid.gen_grid() if not restore else Grid.__static_grid
        self.side = len(self.grid)
        self.parts_locations = self.store_part_locations()
        self.num_parts = len(self.parts_locations)
        if save:
            Grid.__static_grid = self

    def __str__(self):
        s = pformat(self.grid)
        #s += "\n %s" % pformat(self.parts_locations)
        return s

    def __eq__(self, other):
        return self.grid == other.grid

    def __ne__(self, other):
        return self.grid != other.grid

    def store_part_locations(self):
        locations = []
        for i in xrange(len(self.grid)):
            for j in xrange(len(self.grid[i])):
                if self.grid[i][j] == 'R':
                    locations.append((i, j))
        return locations

    def possible_operators(self):
        # TODO handle assembled parts
        motions = ['N', 'E', 'S', 'W']
        n_parts = self.num_parts
        return [zip([part] * 4, motions) for part in xrange(n_parts)]

    @staticmethod
    def gen_grid():
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
        return grid


class WAMP_SearchNode(SearchNode):
    def __init__(self, state, parent_node=None,
                 operator=None, depth=0, path_cost=0):
        '''
        state (Grid) parent_node (WAMP_SearchNode) operators tuple <p,d>
        where p is the robotic part and d is [NSEW], depth (integer), path_cost
        (integer)
        '''
        self.state = state
        self.parent_node = parent_node
        self.operator = operator
        self.depth = depth
        self.path_cost = path_cost


class WAMP_SearchProblem(SearchProblem):
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.operators = self.initial_state.possible_operators()

    def state_space(self, seq_actions):
        pass

    def goal_test(self, state):
        pass

    def path_cost(self, actions):
        pass

    def expand_node(self, node):
        pass


g = Grid()
print g.num_parts
search_problem = WAMP_SearchProblem(g)

print search_problem.operators
