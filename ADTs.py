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
    def __init__(self, operators, initial_state, state_space):
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
    def __init__(self, qing_func):
        raise NotImplementedError("Should have implemented this")

    def __str__(self):
        raise NotImplementedError("Should have implemented this")

    def queue(self, search_nodes):
        ''' Add the search_node(s) to the queue according to the qing func '''
        raise NotImplementedError("Should have implemented this")

    def remove_front(self):
        ''' returns the front node of the queue '''
        raise NotImplementedError("Should have implemented this")


def general_search(search_problem, qing_func):
    start_node = SearchNode(search_problem.initial_state)
    nodes = SearchQueue(qing_func)
    nodes.queue(start_node)
    while True:
        if nodes.empty():
            return False
        node = nodes.remove_front()
        if search_problem.goal_test(node.state):
            return node
        nodes.queue(search_problem.expand_node(node))
