from ADTs import State, SearchNode, SearchProblem
from random import random, randint
from pprint import pprint, pformat
from copy import deepcopy, copy
from search_queues import BFS_Queue, DFS_Queue


class Part:
    def __init__(self, locations):
        self.locations = locations

    def __str__(self):
        s = '['
        for location in self.locations:
            s += "(%d,%d)" % (location[0], location[1])
        s += ']'
        return s

    def __repr__(self):
        return self.__str__()

    def can_assemble(self, other):
        pairwise = [(loc1,loc2) for loc1 in self.locations for loc2 in other.locations]
        for pair in pairwise:
            if sum([abs(v1-v2) for v1,v2 in zip(*pair)]) == 1:
                return True
        return False

    def assemble(self, other):
        if self.can_assemble(other):
            return Part(self.locations + other.locations)
        else:
            print 'WHAT THE FUCK YOU WANT'


class Grid(State):

    def __init__(self, grid=None):
        self.grid = grid or Grid.gen_grid()
        self.side = len(self.grid)
        self.get_parts()

    def get_char(self, i, j):
        #print "i %d, j %d" % (i,j)
        if self.grid[i][j] == 'X':
            return 'X'
        elif self.grid[i][j] == 'R':
            return str([self.parts.index(part) for part in self.parts if [i,j] in part.locations][0])
        else:
            return '_'

    def __str__(self):
        s = ''
        for i in xrange(len(self.grid)):
            for j in xrange(len(self.grid)):
                #print self.get_char(i,j)
                s += self.get_char(i,j)
                s += ' '
            s += "\n" if i != len(self.grid) - 1 else ''

        # s += "\n %s" % pformat(self.parts_locations)
        return s

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.grid == other.grid

    def __ne__(self, other):
        return self.grid != other.grid

    def get_parts(self):
        parts = []
        for i in xrange(len(self.grid)):
            for j in xrange(len(self.grid[i])):
                if self.grid[i][j] == 'R':
                    parts.append(Part([[i, j]]))

        #print "I have %d parts" % len(parts)
        self.parts = parts
        self.assemble_parts()

    def assemble_parts(self):
        first_time = True
        fixed_point = None
        while first_time or not fixed_point:
            fixed_point = True
            first_time = False
            for i in xrange(len(self.parts)):
                for j in xrange(i+1,len(self.parts)):
                    if i == j or self.parts[i] is None or self.parts[j] is None:
                        continue
                    if self.parts[i].can_assemble(self.parts[j]):
                        new_part = self.parts[i].assemble(self.parts[j])
                        self.parts.append(new_part)
                        self.parts[i] = None
                        self.parts[j] = None
                        fixed_point = False

        self.parts = filter(lambda x: x is not None, self.parts)

    @staticmethod
    def delta_direction(direction):
        if direction == 'N':
            delta = [-1, 0]
        elif direction == 'E':
            delta = [0, 1]
        elif direction == 'S':
            delta = [1, 0]
        elif direction == 'W':
            delta = [0, -1]

        return delta

    @staticmethod
    def apply_direction(loc, direction):
        delta = Grid.delta_direction(direction)
        return [v1+v2 for v1,v2 in zip(loc, delta)]

    def feedback(self, location, direction, other_locations=[]):
        new_loc = Grid.apply_direction(location, direction)
        in_range = 0 <= new_loc[0] < len(self.grid)
        in_range &= 0 <= new_loc[1] < len(self.grid)
        if new_loc in other_locations:
            return 'smooth'

        if in_range:
            value = self.grid[new_loc[0]][new_loc[1]]
        else:
            value = 'W'

        if value == '_':
            return 'smooth'
        elif value == 'R':
            return 'robot'
        elif value == 'X':
            return 'obstacle'
        elif value == 'W':
            return 'damage'

    def possible_operators(self):
        motions = ['N', 'E', 'S', 'W']
        n_parts = len(self.parts)
        return [(part, motion) for part in xrange(n_parts) for motion in motions]

    def apply_operator(self, operator):
        ''' returns an array of the new State (Grid) and a feedback '''
        # TODO handle assembled parts
        part = self.parts[operator[0]]
        direction = operator[1]
        locs = sorted(part.locations)

        if direction == 'E' or direction == 'S':
            locs.reverse()

        current_grid = deepcopy(self)

        while True:
            can_move = True
            for loc in locs:
                assembled = list(locs)
                assembled.remove(loc)
                feedback = current_grid.feedback(loc, direction, assembled)
                can_move &= feedback in ['smooth']
                if not can_move:
                    break

            if can_move:
                locs = current_grid.move(locs, direction)
            else:
                return current_grid, feedback

    def move(self, locations, direction):
        new_locations = []
        for location in locations:
            new_loc = Grid.apply_direction(location, direction)
            new_locations.append(new_loc)
            if self.grid[new_loc[0]][new_loc[1]] != '_':
                print 'WAHAAAAAAAAAAAAAAAAAAAAAAAAAAT'

            self.grid[new_loc[0]][new_loc[1]] = 'R'
            self.grid[location[0]][location[1]] = '_'
            self.get_parts()
        return new_locations

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
        return len(state.parts) == 1
        #def has_adj(place1, places):
            #flag = False or len(places) == 0
            #for place2 in places:
                #flag |= (abs(place1[0] - place2[0]) +
                         #abs(place1[1] - place2[1])) == 1
                #if flag:
                    #break
            #return flag

        #adj_parts = []
        #for location in state.parts_locations:
            #if has_adj(location, adj_parts):
                #adj_parts.append(location)
            #else:
                #return False

        #return True

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

#g_ar = [['_', 'R', '_', '_'],
        #['R', '_', 'R', '_'],
        #['_', '_', '_', '_'],
        #['_', 'X', '_', '_']]

#g = Grid(g_ar)
#print g
#print '--------------'
#operator = (1, 'E')
#g2,fb = g.apply_operator(operator)
#print g2
#print fb
#operator = (0, 'S')
#g3,fb = g2.apply_operator(operator)
#print g3
#print fb
#operator = (0, 'E')
#g4,fb = g3.apply_operator(operator)
#print g4
#print fb
##g2 = g.apply_operator(operator)
##print g2
