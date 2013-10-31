from ADTs import State, SearchNode, SearchProblem
from random import random, randint
from pprint import pprint, pformat
from copy import deepcopy, copy
from search_queues import BFS_Queue, DFS_Queue


class Grid(State):

    def __init__(self, grid=None):
        self.grid = grid or Grid.gen_grid()
        self.side = len(self.grid)
        self.parts_locations = self.store_part_locations()
        self.num_parts = len(self.parts_locations)

    def __str__(self):
        s = pformat(self.grid)
        # s += "\n %s" % pformat(self.parts_locations)
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
        ''' returns an array of the new State (Grid) and a feedback '''
        # TODO handle assembled parts

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

        new_grid = deepcopy(self.grid)
        part_number = operator[0]
        old_place = copy(self.parts_locations[part_number])
        feedback = None
        while feedback == 'smooth' or feedback is None:
            new_place = move(old_place, operator[1])
            in_range = 0 <= new_place[0] < len(self.grid)
            in_range &= 0 <= new_place[1] < len(self.grid)

            if in_range:
                old_value = self.grid[new_place[0]][new_place[1]]
            else:
                old_value = 'W'

            feedback = '555'
            if old_value == '_':
                feedback = 'smooth'
            elif old_value == 'X':
                feedback = 'obstacle'
            elif old_value == 'R':  # FIXME handle assemebled pieces
                feedback = 'robot'
            elif old_value == 'W':
                feedback = 'damage'
            else:
                print 'something is terribly wrong'
                pprint(self.grid)

            if feedback == 'smooth':
                new_grid[old_place[0]][old_place[1]] = '_'
                new_grid[new_place[0]][new_place[1]] = 'R'
                old_place = new_place
            elif feedback == 'damage':
                new_grid[old_place[0]][old_place[1]] = 'r'


        return [Grid(new_grid), feedback]

    @staticmethod
    def gen_grid():
        side = randint(4, 5)
        grid = [[random() for _ in xrange(side)] for _ in xrange(side)]

        def mapping(x):
            if x < 0.2:
                return 'R'
            elif x < 0.3:
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

    def __str__(self):
        s = "Node, Depth: %d, operator: %s\n" % (self.depth, self.operator)
        s += format(self.state)
        return s

    def expand(self):
        operators = self.state.possible_operators()
        nodes = []
        for operator in operators:
            new_state, feedback = self.state.apply_operator(operator)
            cost = 1  # FIXME make it depend on the feedback
            if feedback != 'damage':
                new_node = WAMP_SearchNode(new_state,
                                           parent_node=self,
                                           operator=operator,
                                           depth=self.depth + 1,
                                           path_cost=self.path_cost + cost)
                nodes.append(new_node)
        return nodes

    def print_path(self):
        print self
        self.parent_node.print_path() if self.parent_node is not None else None


class WAMP_SearchProblem(SearchProblem):

    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.operators = self.initial_state.possible_operators()

    def state_space(self, seq_actions):
        pass

    def goal_test(self, state):
        def has_adj(place1, places):
            flag = False or len(places) == 0
            for place2 in places:
                flag |= (abs(place1[0] - place2[0]) +
                         abs(place1[1] - place2[1])) == 1
                if flag:
                    break
            return flag

        adj_parts = []
        for location in state.parts_locations:
            if has_adj(location, adj_parts):
                adj_parts.append(location)
            else:
                return False

        return True

    def path_cost(self, actions):
        pass

    def expand_node(self, node):
        return node.expand()


def general_search(search_problem, nodes_q):
    start_node = WAMP_SearchNode(search_problem.initial_state)
    nodes_q.enqueue([start_node])
    while True:
        if len(nodes_q) == 0:
            return False
        node = nodes_q.remove_front()
        #print "%d %d" % (node.depth, len(nodes_q))
        if search_problem.goal_test(node.state):
            return node
        nodes_q.enqueue(search_problem.expand_node(node))


def run():
    g = Grid()
    search_problem = WAMP_SearchProblem(g)
    print g
    print '-----\n\n'

    # nodes_q = BFS_Queue()
    nodes_q = BFS_Queue()
    return general_search(search_problem, nodes_q)

#node = run()
#node.print_path()
