from solver.base import Cube
from solver.cross import check_cross_solved
from solver.f2l import check_f2l_solved
from solver.oll import check_oll_solved
from solver.solve import solve_cross, solve_f2l, solve_oll, solve_pll, check_cube_solved
import pytest

NUM_CROSS_TESTS = 100
NUM_F2L_TESTS = 100
NUM_OLL_TESTS = 100
NUM_PLL_TESTS = 100

def test_cross():
    for _ in range(NUM_CROSS_TESTS):
        cube = Cube.default()
        cube.mix_up()
        cube_string = cube.to_string()
        try:
            solve_cross(cube)
            assert check_cross_solved(cube)
        except Exception as e:
            raise Exception(f"Exception: {e}\nFailed on cube: {cube_string}")


def test_f2l():
    for _ in range(NUM_F2L_TESTS):
        cube = Cube.default()
        cube.mix_up()
        solve_cross(cube, minimize_moves=False)
        cube_string = cube.to_string()
        try:
            solve_f2l(cube)
            assert check_f2l_solved(cube)
        except Exception as e:
            raise Exception(f"Exception: {e}\nFailed on cube: {cube_string}")


def test_oll():
    for _ in range(NUM_OLL_TESTS):
        cube = Cube.default()
        cube.mix_up()
        solve_cross(cube, minimize_moves=False)
        solve_f2l(cube, minimize_moves=False)
        cube_string = cube.to_string()
        try:
            solve_oll(cube)
            assert check_oll_solved(cube)
        except Exception as e:
            raise Exception(f"Exception: {e}\nFailed on cube: {cube_string}")


def test_pll():
    for _ in range(NUM_PLL_TESTS):
        cube = Cube.default()
        cube.mix_up()
        solve_cross(cube, minimize_moves=False)
        solve_f2l(cube, minimize_moves=False)
        solve_oll(cube)
        cube_string = cube.to_string()
        try:
            solve_pll(cube)
            assert check_cube_solved(cube)
        except Exception as e:
            raise Exception(f"Exception: {e}\nFailed on cube: {cube_string}")
