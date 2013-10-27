from ADTs import SearchQueue


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
