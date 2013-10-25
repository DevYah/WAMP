class State(object):
    def __init__(self):
        raise NotImplementedError("Should have implemented this")

    def __str__(self):
        raise NotImplementedError("Should have implemented this")


class SearchNode(object):
    def __init__(self, state, parent_node, operator, depth, path_cost):
        raise NotImplementedError("Should have implemented this")

    def __str__(self):
        raise NotImplementedError("Should have implemented this")


class SearchProblem(object):
    def __init__(self, initial_state):
        '''
        {operators} are accessed via the {self.operators} method
        {state_space} is also not stored, but calculated
        {goal_test} is also used via a method {self.goal_test}
        {path_cost} is also used via a method {self.path_cost}
        '''
        raise NotImplementedError("Should have implemented this")

    def operators(self):
        ''' The list of all possible operators regardless of the state '''
        raise NotImplementedError("Should have implemented this")

    def state_space(self, seq_actions):
        '''
        given a sequence of actions, return a resutling state from
        applying the sequence to the initial state
        '''
        raise NotImplementedError("Should have implemented this")

    def goal_test(self, state):
        ''' checks if the state matches the goal or not'''
        raise NotImplementedError("Should have implemented this")

    def path_cost(self, actions):
        ''' assings cost to the sequence of actions '''
        raise NotImplementedError("Should have implemented this")

    def expand_node(self, node):
        ''' returns a set of nodes resulting from all the operators '''
        raise NotImplementedError("Should have implemented this")


class SearchQueue(object):
    def __init__(self):
        raise NotImplementedError("Should have implemented this")

    def __str__(self):
        raise NotImplementedError("Should have implemented this")

    def __len__(self):
        raise NotImplementedError("Should have implemented this")

    def enqueue(self, nodes):
        ''' Add the search_node(s) to the queue according to the qing func '''
        raise NotImplementedError("Should have implemented this")

    def remove_front(self):
        ''' returns the front node of the queue '''
        raise NotImplementedError("Should have implemented this")
