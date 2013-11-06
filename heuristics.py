

def dist(loc1, loc2):
    return sum([abs(a - b) for (a, b) in zip(loc1, loc2)])


def minimum_dist(part1, part2):
    return min([dist(a, b)
                for a in part1.locations
                for b in part2.locations]) - 1


def heuristic1(node):
    grid = node.state
    return len(grid.parts) - 1


# Sum of the min_dist(Ui) for all Ui in Units and min_dist is defined as
# min([dist(ui,uj) for all ui, uj in units and ui != uj]) - num_of_units
def heuristic3(node):
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
    return sum_of_min_dist - len(units) + len(grid.parts) - 1


def heuristic4(node):
    grid = node.state
    units = map(lambda x: x.locations, grid.parts)
    units = [tuple(u) for l in units for u in l]
    min_dist = 999999999999999
    min_loc = None
    for a in units:
        #print a
        current_dist = 0
        for b in units:
            if b is a:
                continue
            current_dist += dist(a, b) - 1
            #print "\t dist to %s  is %d" % (b, dist(a, b))

        #print "\t\t %d" % current_dist
        if current_dist < min_dist:
            min_dist = current_dist
            min_loc = a

    #print min_loc
    return min_dist


def heuristic2(node):
    parts = node.state.parts
    min_dist = 99999999999
    for p1 in parts:
        dist = 0
        for p2 in parts:
            if p1 is p2:
                continue

            dist += minimum_dist(p1, p2) * len(p2.locations)

        if dist < min_dist:
            min_dist = dist

    return min_dist

# This heuristic tries to assemble nearest parts and considers best case
# scenario in which all parts decrease between the distance  between the
# next part and the original part
# BEST PLACEMENT
def admisisble1(node):
    grid = node.state
    units = map(lambda x: x.locations, grid.parts)
    units = [tuple(u) for l in units for u in l]
    min_sum = 999999999999
    min_loc = None
    min_index = -1
    i = -1
    for unit1 in units:
        i += 1
        currnt_parts_length = 0
        current_dist = 0
        for unit2 in sorted(units, key=lambda x: dist(unit1, x)):
            current_dist += max([0, dist(unit1, unit2) - currnt_parts_length])
            currnt_parts_length += 1

        if current_dist < min_sum:
            min_sum = current_dist
            min_loc = unit1
            min_index = i

    #print min_loc
    #print min_index
    if len(grid.parts) > 1:
        min_sum = max([1, min_sum])

    return min_sum
