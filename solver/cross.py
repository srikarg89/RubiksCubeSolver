from typing import Optional
from .base import Cube, Movement, Color, realign_cube


def check_cross_solved(cube: Cube):
    bottom_color = cube.bottom.center
    # Check that the cross is present on the bottom face
    if not all(c == bottom_color for c in cube.bottom.middle_row):
        return False
    if not all(c == bottom_color for c in cube.bottom.middle_col):
        return False

    # Check that all the side faces have the cross pieces lined up
    side_faces = [cube.front, cube.right, cube.back, cube.left]
    return all(face.bottom_middle == face.center for face in side_faces)


def multi_down(cube: Cube, num_iterations: int):
    num_iterations %= 4
    for _ in range(num_iterations):
        cube.run_movement(Movement.DOWN)


def multi_down_prime(cube: Cube, num_iterations: int):
    # A down prime is just a down 3 times.
    num_iterations *= 3
    num_iterations %= 4
    for _ in range(num_iterations):
        cube.run_movement(Movement.DOWN)


def check_cross_case_solved(cube: Cube, side_color: Color):
    bottom_color = cube.bottom.center
    if cube.front.center == side_color:
        return cube.front.bottom_middle == side_color and cube.bottom.top_middle == bottom_color
    if cube.right.center == side_color:
        return cube.right.bottom_middle == side_color and cube.bottom.middle_right == bottom_color
    if cube.back.center == side_color:
        return cube.back.bottom_middle == side_color and cube.bottom.bottom_middle == bottom_color
    if cube.left.center == side_color:
        return cube.left.bottom_middle == side_color and cube.bottom.middle_left == bottom_color
    return False


def detect_and_solve_cross_case(cube: Cube, target_side_color: Optional[Color] = None):
    """
    If target_side_color is provided, then only solve the case if the complmenting color is the side color.
    6 cases:
        1. piece is on the top side
        2. piece is on the top edge
        3. piece is on the left edge
        4. piece is on the right edge
        5. piece is on the bottom edge
        6. piece is on the bottom but in the wrong spot
    """
    bottom_color = cube.bottom.center
    num_downs_to_front = {
        cube.front.center: 0,
        cube.left.center: 1,
        cube.back.center: 2,
        cube.right.center: 3,
    }

    # Case 1: Piece is on the top side
    if cube.top.bottom_middle == bottom_color:
        complement_color = cube.front.top_middle
        if target_side_color is None or complement_color == target_side_color:
            # We want to insert it at the front
            num_downs = num_downs_to_front[complement_color]
            multi_down(cube, num_downs)
            cube.run_algorithm("F2")
            multi_down_prime(cube, num_downs)
            return True
    # Case 2: Piece is on the top edge
    if cube.front.top_middle == bottom_color:
        complement_color = cube.top.bottom_middle
        if target_side_color is None or complement_color == target_side_color:
            num_downs = num_downs_to_front[complement_color]
            multi_down(cube, num_downs)
            cube.run_algorithm("F D R' D'")
            multi_down_prime(cube, num_downs)
            return True
    # Case 3: Piece is on the left edge
    if cube.front.middle_left == bottom_color:
        complement_color = cube.left.middle_right
        if target_side_color is None or complement_color == target_side_color:
            # We want to insert it on our left
            num_downs = num_downs_to_front[complement_color] - 1
            multi_down(cube, num_downs)
            cube.run_algorithm("L")
            multi_down_prime(cube, num_downs)
            return True
    # Case 4: Piece is on the right edge
    if cube.front.middle_right == bottom_color:
        complement_color = cube.right.middle_left
        if target_side_color is None or complement_color == target_side_color:
            # We want to insert it on our right
            num_downs = num_downs_to_front[complement_color] + 1
            multi_down(cube, num_downs)
            cube.run_algorithm("R'")
            multi_down_prime(cube, num_downs)
            return True
    # Case 5: Piece is on the bottom edge
    if cube.front.bottom_middle == bottom_color:
        complement_color = cube.bottom.top_middle
        if target_side_color is None or complement_color == target_side_color:
            # Bring the piece to the right edge, and then run the regular right edge stuff.
            cube.run_algorithm("F'")
            num_downs = num_downs_to_front[complement_color] + 1
            multi_down(cube, num_downs)
            cube.run_algorithm("R'")
            multi_down_prime(cube, num_downs)
            return True
    # Case 6: Piece is on the bottom side but wrong position
    if cube.bottom.top_middle == bottom_color and cube.front.bottom_middle != cube.front.center:
        complement_color = cube.front.bottom_middle
        if target_side_color is None or complement_color == target_side_color:
            # Bring the piece to the right edge, and then run the regular right edge stuff.
            cube.run_algorithm("D R D'")
            num_downs = num_downs_to_front[complement_color] + 1
            multi_down(cube, num_downs)
            cube.run_algorithm("R'")
            multi_down_prime(cube, num_downs)
            return True
    return False
