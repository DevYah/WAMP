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
    def __init__(self, cost_function):
        self.q = []
        self.cost_function = cost_function

    def __str__(self):
        s = "BestFrist Q"
        s += format(self.q)
        return s

    def __len__(self):
        return len(self.q)

    def enqueue(self, nodes):
        for node in nodes:
            heappush(self.q, (self.cost_function(node), node))

    def remove_front(self):
        return heappop(self.q)[1]
