from ADTs import State, SearchNode, SearchProblem#, SearchQueue
from random import random, randint
from pprint import pprint, pformat
from copy import deepcopy, copy


class Grid(State):

    def __init__(self, grid=None):
        self.grid = grid or Grid.gen_grid()
        self.side = len(self.grid)
        self.parts_locations = self.store_part_locations()
        self.num_parts = len(self.parts_locations)

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
                    locations.append([i, j])
        return locations

    def possible_operators(self):
        # TODO handle assembled parts
        motions = ['N', 'E', 'S', 'W']
        n_parts = self.num_parts
        return [(part, motion) for part in xrange(n_parts) for motion in motions]

    def apply_operator(self, operator):
        # TODO handle assembled parts
        new_grid = deepcopy(self.grid)
        part_number = operator[0]
        old_place = self.parts_locations[part_number]

        def move(old_place, direction):
            new_place = copy(old_place)
            if direction == 'N':
                new_place[0] -= 1
            elif direction == 'E':
                new_place[1] += 1
            elif direction == 'S':
                new_place[0] += 1
            elif direction == 'W':
                new_place[1] -= 1
            return new_place

        new_place = move(old_place, operator[1])
        in_range = 0 <= new_place[0], new_place[0] < len(self.grid)
        in_range = reduce(lambda x, y: x & y, in_range)

        print "old place is %s" % old_place.__str__()
        print "new place is %s" % new_place.__str__()
        old_value = self.grid[new_place[0]][new_place[1]] if in_range else 'barbed'
        print "existig value is %s" % old_value

        feedback = '555'
        if old_value == '_':
            feedback = 'smooth'
        elif old_value == 'X':
            feedback = 'obstacle'
        elif old_value == 'R':  # FIXME handle assemebled pieces
            feedback = 'robot'
        elif not in_range:
            feedback = 'damage'
        else:
            print 'something is terribly wrong'
            pprint(self.grid)

        if feedback == 'smooth':
            new_grid[old_place[0]][old_place[1]] = '_'
            new_grid[new_place[0]][new_place[1]] = 'R'

        return [Grid(new_grid), feedback]

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

    @staticmethod
    def static_grid():
        return Grid.__static_grid


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

    def expand(self):
        operators = self.state.possible_operators()
        pass


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
print g
search_problem = WAMP_SearchProblem(g)
ops = search_problem.operators
op = ops[2]
print 'Applying operator %s' % op.__str__()
place = g.parts_locations[op[0]]
print "moving part %d at (%d,%d) to %s" % (op[0], place[0], place[1], op[1])
after_apply = g.apply_operator(op)
print after_apply[1]
print(after_apply[0])
