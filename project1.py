class State:
    def __init__(self):
        pass

    def __str__(self):
        pass

class SearchNode:
    def __init__(self, state, parent_node, operator, depth, path_cost):
        pass

    def __str__(self):
        pass

class SearchProblem:
    def __init__(self, operators, initial_state, state_space):
        pass

    def goal_test(self, state):
        ''' checks if the state matches the goal or not'''
        pass

    def path_cost(self, actions):
        ''' assings cost to the sequence of actions '''
        pass

    def expand_node(self, node):
        ''' returns a set of nodes resulting from all the operators '''
        pass

class SearchQueue:
    def __init__(self, qing_func):
        pass

    def __str__(self):
        pass

    def queue(self, search_nodes):
        ''' Add the search_node(s) to the queue according to the qing func '''
        pass

    def remove_front(self):
        ''' returns the front node of the queue '''
        pass


def general_search(search_problem, qing_func):
    start_node = SearchNode(search_problem.initial_state)
    nodes = SearchQueue(qing_func)
    nodes.queue(start_node)
    while True:
        if nodes.empty():
            return False
        node = nodes.remove_front()
        if search_problem.goal_test(state):
            return node
        nodes.queue(search_problem.expand_node(node))
