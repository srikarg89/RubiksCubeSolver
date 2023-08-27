# F2L cube.run_algorithms list
# Function name: f2l + corner position + corner orientation + edge position + edge orientation
# https://drive.google.com/file/d/1nzAXYUWZJ6H2wIOXaHdWXep3W57tArbR/view

# Edge positions, assuming Blue is the front side, Red is the right side, Yellow is the top side:
# BY = 1
# OY = 2
# GY = 3
# RY = 4
# BR = 5
# OB = 6
# GO = 7
# RG = 8
# BW = 9
# OW = 10
# GW = 11
# RW = 12
# 
# Edge orientations are named as two letters:
#     - The first letter represents the side that the front-facing color is on.
#     - The second letter represents the side that the right-facing color is on.
# 
# Some examples, assuming the Blue center is the front side, the Red center is the right side, and the Yellow center is the top side:
#     - That means the F2L edge is the Blue-Red Edge.
# FU: Blue is on the front side, red is on the top side.
# RB: Blue is on the right side, red is on the back side.
# 
# 
# Corner orientations are named as three letters:
#     - The first letter represents the side that the front-facing color is on.
#     - The second letter represents the side that the right-facing color is on.
#     - The third letter represents the side that the bottom-facing color is on.
# 
# Some examples, assuming the Blue center is the front side, the Red center is the right side, and the Yellow center is the top side:
#     - That means the F2L corner is the Blue-Red-White Corner.
# FUR: Blue is on the front side, red is on the top side, white is on the right side.
# BLU: Blue is on the back side, red is on the left side, white is on the top side.
# 
# F2L method naming scheme is: f2l_<edge orientation>_<corner orientation>
# For example, an F2L method could be named f2l_FU_BLU

from .base import Cube, Color, Movement, realign_cube

## Section 1 - Basic cases.

# Corner on top, Edge on top -- Section 1A

# White on top

def f2l_UL_RFU(cube: Cube):
    cube.run_algorithm("y F R U2 R' F'")

def f2l_UB_RFU(cube: Cube):
    cube.run_algorithm("U (R U2 R') U (R U' R')")

def f2l_UF_RFU(cube: Cube):
    cube.run_algorithm("U (F R' F' R) U (R U R')")

def f2l_UR_RFU(cube: Cube):
    cube.run_algorithm("(R U2 R') U' (R U R')")

def f2l_BU_RFU(cube: Cube):
    cube.run_algorithm("F' L' U2 L F")

def f2l_LU_RFU(cube: Cube):
    cube.run_algorithm("y U' (L' U2 L) U' (L' U L)")

def f2l_RU_RFU(cube: Cube):
    cube.run_algorithm("F (U R U' R') F' (R U' R')")

def f2l_FU_RFU(cube: Cube):
    cube.run_algorithm("y (L' U2 L) U (L' U' L)")

# White on right

def f2l_UB_FUR(cube: Cube):
    cube.run_algorithm("R U R'")

def f2l_UL_FUR(cube: Cube):
    cube.run_algorithm("U' (R U R') U (R U R')")

def f2l_UF_FUR(cube: Cube):
    cube.run_algorithm("R' U2 R2 U R2' U R")

def f2l_UR_FUR(cube: Cube):
    cube.run_algorithm("U' (R U' R') U (R U R')")

def f2l_FU_FUR(cube: Cube):
    cube.run_algorithm("y U' (L' U L)")

def f2l_BU_FUR(cube: Cube):
    cube.run_algorithm("y U (L' U2 L) U2 (L' U L)")

def f2l_LU_FUR(cube: Cube):
    cube.run_algorithm("y U (L' U' L) U2 (L' U L)")

def f2l_RU_FUR(cube: Cube):
    cube.run_algorithm("(R U' R') y U2 (L' U' L)")

# White in front

def f2l_LU_URF(cube: Cube):
    cube.run_algorithm("y (L' U' L)")

def f2l_BU_URF(cube: Cube):
    cube.run_algorithm("y U (L' U' L) U' (L' U' L)")

def f2l_RU_URF(cube: Cube):
    cube.run_algorithm("y L U2 L2' U' L2 U' L'")

def f2l_FU_URF(cube: Cube):
    cube.run_algorithm("y U (L' U L) U' (L' U' L)")

def f2l_UR_URF(cube: Cube):
    cube.run_algorithm("U (R U' R')")

def f2l_UL_URF(cube: Cube):
    cube.run_algorithm("U' (R U2 R') U2 (R U' R')")

def f2l_UB_URF(cube: Cube):
    cube.run_algorithm("U' (R U R') U2 (R U' R')")

def f2l_UF_URF(cube: Cube):
    cube.run_algorithm("y2 (Fw' L Fw) U2 (L U L')")

# One piece in slot -- Section 1b

# Edge in slot

def f2l_FR_FUR(cube: Cube):
    cube.run_algorithm("U (R U R') U2 (R U R')")

def f2l_FR_URF(cube: Cube):
    cube.run_algorithm("U' R U' R' U2 R U' R'")

def f2l_FR_RFU(cube: Cube):
    cube.run_algorithm("(U R U' R') (U R U' R') (U R U' R')")

def f2l_RF_FUR(cube: Cube):
    cube.run_algorithm("U (F' U' F) U' (R U R')")

def f2l_RF_URF(cube: Cube):
    cube.run_algorithm("U2 (R U R') (F R' F' R)")

def f2l_RF_RFU(cube: Cube):
    cube.run_algorithm("(R U' R') (F' U2 F)")

# Corner in slot

def f2l_UR_DFR(cube: Cube):
    cube.run_algorithm("(R U R') U' (R U R')")

def f2l_UR_RDF(cube: Cube):
    cube.run_algorithm("(R U' R') U (R U' R')")

def f2l_UR_FRD(cube: Cube):
    cube.run_algorithm("U' (R' F R F') (R U R')")

def f2l_FU_RDF(cube: Cube):
    cube.run_algorithm("y (L' U' L) U (L' U' L)")

def f2l_FU_DFR(cube: Cube):
    cube.run_algorithm("y (L' U L) U' (L' U L)")

def f2l_FU_FRD(cube: Cube):
    cube.run_algorithm("y (L F L') (U' L' U L) F'")

# Both pieces in slot -- Section 1C

def f2l_FR_DFR(cube: Cube):
    cube.run_algorithm("(R U' R') U (R U2 R' U R U' R')")

def f2l_FR_RDF(cube: Cube):
    cube.run_algorithm("(R U' R') U' (R U R' U2 R U' R')")

def f2l_RF_DFR(cube: Cube):
    cube.run_algorithm("(R U' R') (F' L' U2 L F)")

def f2l_RF_RDF(cube: Cube):
    cube.run_algorithm("(F' L' U2 L F) (R U R')")

def f2l_RF_FRD(cube: Cube):
    cube.run_algorithm("R2' U2' F R2 F' U2' R' U R'")

# Section 2 -- 1 piece is in the wrong slot.

# Edge is in the wrong slot.

# White stickers face up

def f2l_BR_RFU(cube: Cube):
    cube.run_algorithm("U' R' U R2 U' R'")

def f2l_RB_RFU(cube: Cube):
    cube.run_algorithm("y R' F R2 U' R' U2 F'")

def f2l_FL_RFU(cube: Cube):
    cube.run_algorithm("y U L U' L2' U L")

def f2l_LF_RFU(cube: Cube):
    cube.run_algorithm("L F' L2' U L U2' F")

def f2l_BL_LBU(cube: Cube):
    cube.run_algorithm("y2")
    cube.run_algorithm("U2 L2' Uw L2 Uw' L2'")

def f2l_LB_LBU(cube: Cube):
    cube.run_algorithm("y2")
    cube.run_algorithm("L F' U F L'")

# White stickers face side / front

def f2l_BR_FUR(cube: Cube):
    cube.run_algorithm("R' U' R2 U R'")

def f2l_RB_FUR(cube: Cube):
    cube.run_algorithm("F D R D' F'")

def f2l_FL_FUR(cube: Cube):
    cube.run_algorithm("U' (L' U' L) (R U' R')")

def f2l_LF_FUR(cube: Cube):
    cube.run_algorithm("(F U2 F') (R U R')")

def f2l_BL_BUL(cube: Cube):
    cube.run_algorithm("y2")
    cube.run_algorithm("U (R U R') (L U L')")

def f2l_LB_BUL(cube: Cube):
    cube.run_algorithm("y2")
    cube.run_algorithm("U2 F' (L U L') F")

def f2l_FL_URF(cube: Cube):
    cube.run_algorithm("y L U L2' U' L")

def f2l_LF_URF(cube: Cube):
    cube.run_algorithm("L' (F' U' F) L")

def f2l_BR_URF(cube: Cube):
    cube.run_algorithm("y U (R U R') (L' U L)")

def f2l_RB_URF(cube: Cube):
    cube.run_algorithm("R' U2 R F' U' F")

def f2l_BL_ULB(cube: Cube):
    cube.run_algorithm("y2")
    cube.run_algorithm("U' (R U' R') (L U' L')")

def f2l_LB_ULB(cube: Cube):
    cube.run_algorithm("y2")
    cube.run_algorithm("U2' R (B' U' B) R'")

# Section 2B - Corner is in the wrong slot

# Corner is in the right slot

def f2l_RU_RBD(cube: Cube):
    cube.run_algorithm("y")
    cube.run_algorithm("U (R U' R') (L' U L)")

def f2l_RU_BDR(cube: Cube):
    cube.run_algorithm("y")
    cube.run_algorithm("U2 (R U' R') U (L' U' L)")

def f2l_RU_DRB(cube: Cube):
    cube.run_algorithm("y")
    cube.run_algorithm("(R U R') U' (L' U L)")

def f2l_UR_RBD(cube: Cube):
    cube.run_algorithm("y")
    cube.run_algorithm("y (L' U2 L) U' (L U L')")

def f2l_UR_BDR(cube: Cube):
    cube.run_algorithm("y")
    cube.run_algorithm("y U' L' U' L2 U2 L'")

def f2l_UR_DRB(cube: Cube):
    cube.run_algorithm("y")
    cube.run_algorithm("U' (R U R') (F U F')")

# Corner is in the left slot

def f2l_UF_LFD(cube: Cube):
    cube.run_algorithm("y'")
    cube.run_algorithm("y U' (L' U L) (R U' R')")

def f2l_UF_DLF(cube: Cube):
    cube.run_algorithm("y'")
    cube.run_algorithm("(F R' F' R) U (R' U2 R)")

def f2l_UF_FDL(cube: Cube):
    cube.run_algorithm("y'")
    cube.run_algorithm("y (L' U' L) U (R U' R')")

def f2l_FU_LFD(cube: Cube):
    cube.run_algorithm("y'")
    cube.run_algorithm("(R U2 R') U (R' U' R)")

def f2l_FU_DLF(cube: Cube):
    cube.run_algorithm("y'")
    cube.run_algorithm("U R U R2' U2 R")

def f2l_FU_FDL(cube: Cube):
    cube.run_algorithm("y'")
    cube.run_algorithm("U' (R U' R') U' (R' U' R)")

# Corner is in the opposite slot

def f2l_UL_BLD(cube: Cube):
    cube.run_algorithm("y2")
    cube.run_algorithm("U' (F' U F) (L U2 L')")

def f2l_UL_LDB(cube: Cube):
    cube.run_algorithm("y2")
    cube.run_algorithm("(R U' R') (L U2 L')")

def f2l_UF_DBL(cube: Cube):
    cube.run_algorithm("y2")
    cube.run_algorithm("R U2 R' L U L'")

def f2l_BU_BLD(cube: Cube):
    cube.run_algorithm("y2")
    cube.run_algorithm("y U (F U' F') (R' U2 R)")

def f2l_BU_DBL(cube: Cube):
    cube.run_algorithm("y2")
    cube.run_algorithm("y (L' U L) (R' U2 R)")

def f2l_BU_LDB(cube: Cube):
    cube.run_algorithm("y2")
    cube.run_algorithm("y (L' U' L) U' (R' U' R)")

F2L_FUNCTION_MAP = {
    ('UL', 'RFU'): f2l_UL_RFU,
    ('UB', 'RFU'): f2l_UB_RFU,
    ('UF', 'RFU'): f2l_UF_RFU,
    ('UR', 'RFU'): f2l_UR_RFU,
    ('BU', 'RFU'): f2l_BU_RFU,
    ('LU', 'RFU'): f2l_LU_RFU,
    ('RU', 'RFU'): f2l_RU_RFU,
    ('FU', 'RFU'): f2l_FU_RFU,
    ('UB', 'FUR'): f2l_UB_FUR,
    ('UL', 'FUR'): f2l_UL_FUR,
    ('UF', 'FUR'): f2l_UF_FUR,
    ('UR', 'FUR'): f2l_UR_FUR,
    ('FU', 'FUR'): f2l_FU_FUR,
    ('BU', 'FUR'): f2l_BU_FUR,
    ('LU', 'FUR'): f2l_LU_FUR,
    ('RU', 'FUR'): f2l_RU_FUR,
    ('LU', 'URF'): f2l_LU_URF,
    ('BU', 'URF'): f2l_BU_URF,
    ('RU', 'URF'): f2l_RU_URF,
    ('FU', 'URF'): f2l_FU_URF,
    ('UR', 'URF'): f2l_UR_URF,
    ('UL', 'URF'): f2l_UL_URF,
    ('UB', 'URF'): f2l_UB_URF,
    ('UF', 'URF'): f2l_UF_URF,
    ('FR', 'FUR'): f2l_FR_FUR,
    ('FR', 'URF'): f2l_FR_URF,
    ('FR', 'RFU'): f2l_FR_RFU,
    ('RF', 'FUR'): f2l_RF_FUR,
    ('RF', 'URF'): f2l_RF_URF,
    ('RF', 'RFU'): f2l_RF_RFU,
    ('UR', 'DFR'): f2l_UR_DFR,
    ('UR', 'RDF'): f2l_UR_RDF,
    ('UR', 'FRD'): f2l_UR_FRD,
    ('FU', 'RDF'): f2l_FU_RDF,
    ('FU', 'DFR'): f2l_FU_DFR,
    ('FU', 'FRD'): f2l_FU_FRD,
    ('FR', 'DFR'): f2l_FR_DFR,
    ('FR', 'RDF'): f2l_FR_RDF,
    ('RF', 'DFR'): f2l_RF_DFR,
    ('RF', 'RDF'): f2l_RF_RDF,
    ('RF', 'FRD'): f2l_RF_FRD,
    ('RB', 'RFU'): f2l_RB_RFU,
    ('BR', 'RFU'): f2l_BR_RFU,
    ('FL', 'RFU'): f2l_FL_RFU,
    ('LF', 'RFU'): f2l_LF_RFU,
    ('BL', 'LBU'): f2l_BL_LBU,
    ('LB', 'LBU'): f2l_LB_LBU,
    ('BR', 'FUR'): f2l_BR_FUR,
    ('RB', 'FUR'): f2l_RB_FUR,
    ('FL', 'FUR'): f2l_FL_FUR,
    ('LF', 'FUR'): f2l_LF_FUR,
    ('BL', 'BUL'): f2l_BL_BUL,
    ('LB', 'BUL'): f2l_LB_BUL,
    ('FL', 'URF'): f2l_FL_URF,
    ('LF', 'URF'): f2l_LF_URF,
    ('BR', 'URF'): f2l_BR_URF,
    ('RB', 'URF'): f2l_RB_URF,
    ('BL', 'ULB'): f2l_BL_ULB,
    ('LB', 'ULB'): f2l_LB_ULB,
    ('RU', 'RBD'): f2l_RU_RBD,
    ('RU', 'BDR'): f2l_RU_BDR,
    ('RU', 'DRB'): f2l_RU_DRB,
    ('UR', 'RBD'): f2l_UR_RBD,
    ('UR', 'BDR'): f2l_UR_BDR,
    ('UR', 'DRB'): f2l_UR_DRB,
    ('UF', 'LFD'): f2l_UF_LFD,
    ('UF', 'DLF'): f2l_UF_DLF,
    ('UF', 'FDL'): f2l_UF_FDL,
    ('FU', 'LFD'): f2l_FU_LFD,
    ('FU', 'DLF'): f2l_FU_DLF,
    ('FU', 'FDL'): f2l_FU_FDL,
    ('UL', 'BLD'): f2l_UL_BLD,
    ('UL', 'LDB'): f2l_UL_LDB,
    ('UF', 'DBL'): f2l_UF_DBL,
    ('BU', 'BLD'): f2l_BU_BLD,
    ('BU', 'LDB'): f2l_BU_LDB,
    ('BU', 'DBL'): f2l_BU_DBL,
}


def find_edge_orientation(cube: Cube, c1: Color, c2: Color):
    edge_map = {
        (cube.front.top_middle, cube.top.bottom_middle): 'FU',
        (cube.right.top_middle, cube.top.middle_right): 'RU',
        (cube.back.top_middle, cube.top.top_middle): 'BU',
        (cube.left.top_middle, cube.top.middle_left): 'LU',
        (cube.front.middle_right, cube.right.middle_left): 'FR',
        (cube.right.middle_right, cube.back.middle_left): 'RB',
        (cube.back.middle_right, cube.left.middle_left): 'BL',
        (cube.left.middle_right, cube.front.middle_left): 'LF',
        (cube.front.bottom_middle, cube.bottom.top_middle): 'FD',
        (cube.right.bottom_middle, cube.bottom.middle_right): 'RD',
        (cube.back.bottom_middle, cube.bottom.bottom_middle): 'BD',
        (cube.left.bottom_middle, cube.bottom.middle_left): 'LD',
    }
    if (c1, c2) in edge_map:
        return edge_map[(c1, c2)]
    if (c2, c1) in edge_map:
        val = edge_map[(c2, c1)]
        return val[1] + val[0]
    raise ValueError(f"C1, C2 not found in edge map. C1: {c1}, C2: {c2}\nEdge map: {edge_map}")


def find_corner_orientation(cube: Cube, c1: Color, c2: Color, c3: Color):
    corner_map = {
        (cube.front.top_right, cube.right.top_left, cube.top.bottom_right): 'FRU',
        (cube.front.top_left, cube.left.top_right, cube.top.bottom_left): 'FLU',
        (cube.back.top_left, cube.right.top_right, cube.top.top_right): 'BRU',
        (cube.back.top_right, cube.left.top_left, cube.top.top_left): 'BLU',
        (cube.front.bottom_right, cube.right.bottom_left, cube.bottom.top_right): 'FRD',
        (cube.front.bottom_left, cube.left.bottom_right, cube.bottom.top_left): 'FLD',
        (cube.back.bottom_left, cube.right.bottom_right, cube.bottom.bottom_right): 'BRD',
        (cube.back.bottom_right, cube.left.bottom_left, cube.bottom.bottom_left): 'BLD',
    }
    if (c1, c2, c3) in corner_map:
        return corner_map[(c1, c2, c3)]
    if (c1, c3, c2) in corner_map:
        val = corner_map[(c1, c3, c2)]
        return val[0] + val[2] + val[1]
    if (c3, c2, c1) in corner_map:
        val = corner_map[(c3, c2, c1)]
        return val[2] + val[1] + val[0]
    if (c2, c1, c3) in corner_map:
        val = corner_map[(c2, c1, c3)]
        return val[1] + val[0] + val[2]
    if (c2, c3, c1) in corner_map:
        val = corner_map[(c2, c3, c1)]
        return val[2] + val[0] + val[1]
    if (c3, c1, c2) in corner_map:
        val = corner_map[(c3, c1, c2)]
        return val[1] + val[2] + val[0]
    raise ValueError(f"C1, C2, C3 not found in corner map. C1: {c1}, C2: {c2}, C3: {c3}\nCorner map: {corner_map}")

def position_matches(orientation_1: str, orientation_2):
    return set(orientation_1) == set(orientation_2)


def move_edge_out_of_slot(cube: Cube, edge_orientation: str):
    if position_matches(edge_orientation, 'FR'):
        cube.run_algorithm("R U R'")
        return
    if position_matches(edge_orientation, 'FL'):
        cube.run_algorithm("L' U L")
        return
    if position_matches(edge_orientation, 'BR'):
        cube.run_algorithm("R' U R")
        return
    if position_matches(edge_orientation, 'BL'):
        cube.run_algorithm("L U L'")
        return
    raise ValueError(f"Edge is not in slot: {edge_orientation}")

def move_corner_out_of_slot(cube: Cube, corner_orientation: str):
    if position_matches(corner_orientation, 'DFR'):
        cube.run_algorithm("R U R'")
        return
    if position_matches(corner_orientation, 'DFL'):
        cube.run_algorithm("L' U L")
        return
    if position_matches(corner_orientation, 'DBR'):
        cube.run_algorithm("R' U R")
        return
    if position_matches(corner_orientation, 'DBL'):
        cube.run_algorithm("L U L'")
        return
    raise ValueError(f"Corner is not in slot: {corner_orientation}")

def check_f2l_case_solved(cube: Cube, front_color: Color):
    realign_cube(cube, front_color)
    return (cube.front.center == cube.front.middle_right == cube.front.bottom_right and 
            cube.right.center == cube.right.middle_left == cube.right.bottom_left and
            cube.bottom.center == cube.bottom.top_right)

def check_f2l_solved(cube: Cube):
    side_colors = [cube.front.center, cube.right.center, cube.back.center, cube.left.center]
    for color in side_colors:
        if not check_f2l_case_solved(cube, color):
            return False
    return True

def detect_and_solve_f2l_case(cube: Cube, front_color: Color):
    "If target_side_color is provided, then only solve the case if the complmenting color is the side color."
    realign_cube(cube, front_color)
    front_color = cube.front.center
    right_color = cube.right.center
    bottom_color = cube.bottom.center

    if check_f2l_case_solved(cube, front_color):
        return True

    edge_orientation = find_edge_orientation(cube, front_color, right_color)
    corner_orientation = find_corner_orientation(cube, front_color, right_color, bottom_color)
    # If edge in slot
    if 'U' not in edge_orientation:
        # If corner in slot
        if 'U' not in corner_orientation:
            edge_in_correct_slot = sorted(edge_orientation) == 'FR'
            corner_in_correct_slot = sorted(corner_orientation) == 'DFR'
            # If edge is in correct slot but corner is not, move the corner out of its slot.
            if edge_in_correct_slot and not corner_in_correct_slot:
                move_corner_out_of_slot(cube, corner_orientation)
            # IF edge isn't in correct slot, move it out of its slot.
            elif not edge_in_correct_slot:
                move_edge_out_of_slot(cube, edge_orientation)

    for _ in range(4):
        edge_orientation = find_edge_orientation(cube, front_color, right_color)
        corner_orientation = find_corner_orientation(cube, front_color, right_color, bottom_color)
        if (edge_orientation, corner_orientation) in F2L_FUNCTION_MAP:
            func = F2L_FUNCTION_MAP[(edge_orientation, corner_orientation)]
            func(cube)
            return True
        cube.run_movement(Movement.UP)
    return False

