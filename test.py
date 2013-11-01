from WAMP import *

def test_apply_operator_damadge():
    grid_ar = [['R', '_', '_'], ['_'] * 3, ['_'] * 3]
    g = Grid(grid_ar)
    #node = WAMP_SearchNode(g)
    new_grid, feedback = g.apply_operator((0, 'N'))
    assert feedback == 'damage'
    assert new_grid.grid == [['R', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    new_grid, feedback = g.apply_operator((0, 'E'))
    assert feedback == 'damage'
    assert new_grid.grid == [['_', '_', 'R'], ['_', '_', '_'], ['_', '_', '_']]

    new_grid, feedback = g.apply_operator((0, 'S'))
    assert feedback == 'damage'
    assert new_grid.grid == [['_', '_', '_'], ['_', '_', '_'], ['R', '_', '_']]
    print 'PASSES DAMAGE TEST'


def test_apply_operator_obstacle():
    grid_ar = [['R', '_', 'X'], ['_', '_', '_'], ['X', '_', '_']]
    g = Grid(grid_ar)
    new_grid, feedback = g.apply_operator((0, 'E'))
    assert feedback == 'obstacle'
    assert new_grid.grid == [['_', 'R', 'X'], ['_', '_', '_'], ['X', '_', '_']]

    grid_ar = [['R', '_', 'X'], ['_', '_', '_'], ['X', '_', '_']]
    g = Grid(grid_ar)
    new_grid, feedback = g.apply_operator((0, 'S'))
    assert feedback == 'obstacle'
    assert new_grid.grid == [['_', '_', 'X'], ['R', '_', '_'], ['X', '_', '_']]

    grid_ar = [['R', 'X', 'X'], ['X', '_', '_'], ['X', '_', '_']]
    g = Grid(grid_ar)
    new_grid, feedback = g.apply_operator((0, 'S'))
    assert feedback == 'obstacle'
    assert new_grid.grid == [['R', 'X', 'X'], ['X', '_', '_'], ['X', '_', '_']]

    grid_ar = [['R', '_', 'X'], ['X', '_', '_'], ['X', '_', '_']]
    g = Grid(grid_ar)
    new_grid, feedback = g.apply_operator((0, 'S'))
    assert feedback == 'obstacle'
    assert new_grid.grid == [['R', '_', 'X'], ['X', '_', '_'], ['X', '_', '_']]
    print 'PASSES OBSTACLE TEST'


def test_bfs_solution_simple1():
    g_ar = [['_', 'X', '_'],
            ['R', '_', '_'],
            ['_', 'R', '_']]
    g = Grid(g_ar)
    search_problem = WAMP_SearchProblem(g)
    nodes_q = BFS_Queue()
    goal_node = general_search(search_problem, nodes_q)
    assert search_problem.goal_test(goal_node.state)
    print 'PASSES BFS SIMPLE1'


def test_bfs_solution_simple2():
    g_ar = [['_', 'X', '_'],
            ['R', '_', 'X'],
            ['_', 'R', '_']]
    g = Grid(g_ar)
    search_problem = WAMP_SearchProblem(g)
    nodes_q = BFS_Queue()
    goal_node = general_search(search_problem, nodes_q)
    goal_node = general_search(search_problem, nodes_q)
    print 'PASSES BFS SIMPLE2'

def test_dfs_solution_simple1():
    g_ar = [['_', 'X', '_'],
            ['R', '_', '_'],
            ['_', 'R', '_']]
    g = Grid(g_ar)
    search_problem = WAMP_SearchProblem(g)
    nodes_q = DFS_Queue()
    goal_node = general_search(search_problem, nodes_q)
    assert search_problem.goal_test(goal_node.state)
    print 'PASSES BFS SIMPLE1'

def test_dfs_solution_simple2():
    g_ar = [['_', 'X', '_'],
            ['R', '_', 'X'],
            ['_', 'R', '_']]
    g = Grid(g_ar)
    search_problem = WAMP_SearchProblem(g)
    nodes_q = DFS_Queue()
    goal_node = general_search(search_problem, nodes_q)
    goal_node = general_search(search_problem, nodes_q)
    print 'PASSES BFS SIMPLE2'

test_apply_operator_damadge()
test_apply_operator_obstacle()
test_bfs_solution_simple1()
test_bfs_solution_simple2()
test_dfs_solution_simple1()
test_dfs_solution_simple2()
