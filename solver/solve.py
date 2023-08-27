import random
import itertools
from typing import Iterable
from .base import Cube, Movement, Color
from .cross import detect_and_solve_cross_case, check_cross_solved, check_cross_case_solved
from .f2l import detect_and_solve_f2l_case, check_f2l_case_solved, check_f2l_solved
from .oll import detect_and_run_oll_case, check_oll_solved
from .pll import detect_and_run_pll_case


def check_cube_solved(cube: Cube):
   return all(face.is_solved() for face in [cube.front, cube.back, cube.left, cube.right, cube.top, cube.bottom])


def solve_cross_given_permutation(cube: Cube, permutation: Iterable[Color]):
    # Try solving in the orders of each permutations, and pick the one that solves it with the fewest moves.
    # Check if any of the cross orientations will match. Rotate the cube in all directions.
    for color in permutation:
        if check_cross_case_solved(cube, color):
            continue
        for _ in range(4):
            if detect_and_solve_cross_case(cube, color):
                break
            cube.run_movement(Movement.YAW_CUBE_CW)


def solve_cross(cube: Cube, minimize_moves=True):
    # Find all the side center pieces, and all permutations of that list.
    side_colors = [cube.front.center, cube.right.center, cube.back.center, cube.left.center]

    # If we want to minimize the number of moves to solve cross, try every permutation. Otherwise, just use the default permutation.
    if minimize_moves:
        side_permutations = list(itertools.permutations(side_colors))
    else:
        side_permutations = [side_colors]

    fewest_turns = float("inf")
    fewest_turn_permutation = side_permutations[0]

    # Solve the cross with each permutation, and count how many turns it takes to solve the cube.
    for permutation in side_permutations:
        cube_copy = cube.copy()
        cube_copy.reset_history()
        solve_cross_given_permutation(cube_copy, permutation)
        num_turns = cube_copy.num_turns_in_move_history()
        if num_turns < fewest_turns:
            fewest_turns = num_turns
            fewest_turn_permutation = permutation

    # Apply the best permutation.
    solve_cross_given_permutation(cube, fewest_turn_permutation)


def solve_f2l_given_permutation(cube: Cube, permutation: Iterable[Color]):    
    # Try solving in the orders of each permutations, and pick the one that solves it with the fewest moves.
    # Check if any of the cross orientations will match. Rotate the cube in all directions.
    for color in permutation:
        detect_and_solve_f2l_case(cube, color)
        assert check_f2l_case_solved(cube, color)


def solve_f2l(cube: Cube, minimize_moves=True):
    if not check_cross_solved(cube):
      raise ValueError("Cross must be solved before attempting to solve F2L")

    # Find all the side center pieces, and all permutations of that list.
    side_colors = [cube.front.center, cube.right.center, cube.back.center, cube.left.center]

    # If we want to minimize the number of moves to solve cross, try every permutation. Otherwise, just use the default permutation.
    if minimize_moves:
        side_permutations = list(itertools.permutations(side_colors))
    else:
        side_permutations = [side_colors]

    fewest_turns = float("inf")
    fewest_turn_permutation = side_permutations[0]

    # Solve the cross with each permutation, and count how many turns it takes to solve the cube.
    for permutation in side_permutations:
        cube_copy = cube.copy()
        cube_copy.reset_history()
        solve_f2l_given_permutation(cube_copy, permutation)
        num_turns = cube_copy.num_turns_in_move_history()
        if num_turns < fewest_turns:
            fewest_turns = num_turns
            fewest_turn_permutation = permutation

    # Apply the best permutation.
    solve_f2l_given_permutation(cube, fewest_turn_permutation)


def solve_oll(cube: Cube):
    if not check_cross_solved(cube):
        raise ValueError("Cross must be solved before attempting to solve OLL")

    if not check_f2l_solved(cube):
        raise ValueError("F2L must be solved before attempting to solve OLL")

    # Check if any of the OLL orientations will match. Rotate the cube in all directions.
    for _ in range(4):
        if detect_and_run_oll_case(cube):
            return
        cube.run_movement(Movement.YAW_CUBE_CW)
    raise RuntimeError("Failed to solve OLL")



def solve_pll(cube: Cube):
    if not check_cross_solved(cube):
        raise ValueError("Cross must be solved before attempting to solve PLL")

    if not check_f2l_solved(cube):
        raise ValueError("F2L must be solved before attempting to solve PLL")

    if not check_oll_solved(cube):
        raise ValueError("OLL must be solved before attempting to solve PLL")

    # Check if any of the PLL orientations will match. Rotate the cube in all directions, and also do an UP move in all orientations.
    for _ in range(4):
        for _ in range(4):
            if detect_and_run_pll_case(cube):
                return
            cube.run_movement(Movement.YAW_CUBE_CW)
        cube.run_movement(Movement.UP)

    raise RuntimeError("Failed to solve PLL")


def mix_up_cube(cube: Cube):
    for _ in range(100):
        rand_move = random.choice(list(Movement))
        cube.run_movement(rand_move)


def solve_cube(cube: Cube):
    solve_cross(cube)
    solve_f2l(cube)
    solve_oll(cube)
    solve_pll(cube)

