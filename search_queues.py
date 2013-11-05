from ADTs import SearchQueue
from heapq import heappush, heappop


class BFS_Queue(SearchQueue):
    def __init__(self):
        self.q = []

    def __str__(self):
        s = "BFS Q"
        s += format(self.q)
        return s

    def __len__(self):
        return len(self.q)

    def enqueue(self, nodes):
        for node in nodes:
            self.q.append(node)

    def remove_front(self):
        return self.q.pop(0)


class DFS_Queue(SearchQueue):
    def __init__(self):
        self.q = []

    def __str__(self):
        s = "DFS Q"
        s += format(self.q)
        return s

    def __len__(self):
        return len(self.q)

    def enqueue(self, nodes):
        for node in nodes:
            self.q.append(node)

    def remove_front(self):
        return self.q.pop()


class BestFirst_Queue(SearchQueue):
    def __init__(self, cost_function, a_star=False):
        self.q = []
        self.cost_function = cost_function
        self.a_star = a_star

    def __str__(self):
        s = "BestFrist Q"
        s += format(self.q)
        return s

    def __len__(self):
        return len(self.q)

    def enqueue(self, nodes):
        for node in nodes:
            cost = self.cost_function(node)
            if self.a_star:
                cost += (node.path_cost)
            heappush(self.q, (cost, node))

    def remove_front(self):
        cost, node = heappop(self.q)
        if self.a_star:
            print 'Node pop %d, path_cost: %d, heuristic: %d' % (cost, node.path_cost, cost-node.path_cost)
        else:
            print 'heuristic: %d' % (cost)
        return node
