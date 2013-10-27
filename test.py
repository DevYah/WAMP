from WAMP import *


def test_apply_operator_damadge():
    grid_ar = [['R', '_', '_'], ['_'] * 3, ['_'] * 3]
    g = Grid(grid_ar)
    #node = WAMP_SearchNode(g)
    new_grid, feedback = g.apply_operator((0, 'N'))
    assert feedback == 'damage'
    assert new_grid.grid == [['r', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    new_grid, feedback = g.apply_operator((0, 'E'))
    assert feedback == 'damage'
    assert new_grid.grid == [['_', '_', 'r'], ['_', '_', '_'], ['_', '_', '_']]

    new_grid, feedback = g.apply_operator((0, 'S'))
    assert feedback == 'damage'
    assert new_grid.grid == [['_', '_', '_'], ['_', '_', '_'], ['r', '_', '_']]
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

test_apply_operator_damadge()
test_apply_operator_obstacle()
