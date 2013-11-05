

def dist(loc1, loc2):
    return sum([abs(a - b) for (a, b) in zip(loc1, loc2)])


def heuristic1(node):
    grid = node.state
    return len(grid.parts) - 1


# Sum of the min_dist(Ui) for all Ui in Units and min_dist is defined as
# min([dist(ui,uj) for all ui, uj in units and ui != uj]) - num_of_units
def heuristic2(node):
    grid = node.state
    units = map(lambda x: x.locations, grid.parts)
    units = [tuple(u) for l in units for u in l]
    sum_of_min_dist = 0
    for a in units:
        min_dist = grid.side * 2
        for b in units:
            if a is b:
                continue
            if dist(a, b) < min_dist:
                min_dist = dist(a, b)

        sum_of_min_dist += min_dist
    return sum_of_min_dist - len(units)
