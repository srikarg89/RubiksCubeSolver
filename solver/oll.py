# SOURCE: http://www.cubewhiz.com/oll.php
from typing import List
from enum import Enum, auto
from .base import Cube, Movement

# Only Corner Stuff

def alg1(cube: Cube):
  cube.run_algorithm("(R U2) (R2 F R F') U2 (R' F R F')")


def alg2(cube: Cube):
  cube.run_algorithm("F (R U R' U') S (R U R' U') Fw'")


def alg3(cube: Cube):
  cube.run_algorithm("Fw (R U R' U') Fw' U' F (R U R' U') F'")


def alg4(cube: Cube):
  cube.run_algorithm("Fw (R U R' U') Fw' U F (R U R' U') F'")


def alg5(cube: Cube):
  cube.run_algorithm("(Rw' U2) (R U R' U Rw)")


def alg6(cube: Cube):
  cube.run_algorithm("(Rw U2) (R' U' R U' Rw')")


def alg7(cube: Cube):
  cube.run_algorithm("	(Rw U R' U) (R U2 Rw')")


def alg8(cube: Cube):
  cube.run_algorithm("(Rw' U' R U') (R' U2 Rw)")


def alg9(cube: Cube):
  cube.run_algorithm("(R U R' U' R' F) (R2 U R' U' F')")


def alg10(cube: Cube):
  cube.run_algorithm("(R U R' U) (R' F R F') (R U2 R')")


def alg11(cube: Cube):
  cube.run_algorithm("Rw' (R2 U R' U R U2 R') U M'")


def alg12(cube: Cube):
  cube.run_algorithm("(M U2) (R' U' R U') (R' U2 R) U M'")


def alg13(cube: Cube):
  cube.run_algorithm("(Rw U' Rw' U' Rw U Rw' y' (R' U R)")


def alg14(cube: Cube):
  cube.run_algorithm("(R' F) (R U R' F' R) y' (R U' R')")


def alg15(cube: Cube):
  cube.run_algorithm("(Lw' U' Lw) (L' U' L U) (Lw' U Lw)")


def alg16(cube: Cube):
  cube.run_algorithm("(Rw U Rw') (R U R' U') (Rw U' Rw')")


def alg17(cube: Cube):
  cube.run_algorithm("(R U R' U) (R' F R F') U2 (R' F R F')")


def alg18(cube: Cube):
  cube.run_algorithm("F (R U R' U) y' (R' U2) (R' F R F')")


def alg19(cube: Cube):
  cube.run_algorithm("Rw' (R U) (R U R' U' Rw) x (R2' U) (R U')")


def alg20(cube: Cube):
  cube.run_algorithm("Rw' (R U) (R U R' U' Rw2) (R2' U) (R U') Rw'")


def alg21(cube: Cube):
  cube.run_algorithm("(R U2) (R' U' R U R' U' R U' R')")


def alg22(cube: Cube):
  cube.run_algorithm("(R U2') (R2' U') (R2 U') (R2' U2' R)")


def alg23(cube: Cube):
  cube.run_algorithm("(R2' D) (R' U2) (R D') (R' U2 R')")


def alg24(cube: Cube):
  cube.run_algorithm("(Lw' U') (L U) (R U') (Rw' F)")


def alg25(cube: Cube):
  cube.run_algorithm("(R' F) (R B') (R' F') (R B)")


def alg26(cube: Cube):
  cube.run_algorithm("(R U2) (R' U' R U' R')")


def alg27(cube: Cube):
  cube.run_algorithm("(R U R' U) (R U2 R')")


def alg28(cube: Cube):
  cube.run_algorithm("(M' U M) U2 (M' U M)")


def alg29(cube: Cube):
  cube.run_algorithm("(L2 U' L B) (L' U) (L2 U') (Rw' U' Rw))")


def alg30(cube: Cube):
  cube.run_algorithm("(R2' U R' B') (R U') (R2' U) (Lw U Lw')")


def alg31(cube: Cube):
  cube.run_algorithm("(R' U') F (U R U' R') F' R")


def alg32(cube: Cube):
  cube.run_algorithm("(R Dw) (L' Dw') (R' U) (Lw U Lw')")


def alg33(cube: Cube):
  cube.run_algorithm("(R U R' U') (R' F R F')")


def alg34(cube: Cube):
  cube.run_algorithm("(R U R2' U') (R' F) (R U) (R U') F'")


def alg35(cube: Cube):
  cube.run_algorithm("(R U2) (R2 F) (R F' R U2 R')")


def alg36(cube: Cube):
  cube.run_algorithm("(L' U' L U') (L' U L U) (L F' L' F)")


def alg37(cube: Cube):
  cube.run_algorithm("F (R U') (R' U' R U) (R' F')")


def alg38(cube: Cube):
  cube.run_algorithm("(R U R' U) (R U' R' U') (R' F R F')")


def alg39(cube: Cube):
  cube.run_algorithm("(L F') (L' U' L U) F U' L'")


def alg40(cube: Cube):
  cube.run_algorithm("(R' F) (R U R' U') F' U R")


def alg41(cube: Cube):
  cube.run_algorithm("(R U') (R' U2) (R U) y (R U') (R' U' F'))")


def alg42(cube: Cube):
  cube.run_algorithm("(L' U) (L U2') (L' U') y' (L' U) (L U F))")


def alg43(cube: Cube):
  cube.run_algorithm("Fw' (L' U' L U) Fw")


def alg44(cube: Cube):
  cube.run_algorithm("Fw (R U R' U') Fw'")


def alg45(cube: Cube):
  cube.run_algorithm("F (R U R' U') F'")


def alg46(cube: Cube):
  cube.run_algorithm("(R' U') (R' F R F') (U R)")


def alg47(cube: Cube):
  cube.run_algorithm("F' (L' U' L U) (L' U' L U) F")


def alg48(cube: Cube):
  cube.run_algorithm("F (R U R' U') (R U R' U') F'")


def alg49(cube: Cube):
  cube.run_algorithm("(R' F R' F' R2) U2 y (R' F R F')")


def alg50(cube: Cube):
  cube.run_algorithm("(R B' R B R2') U2 (F R' F' R))")


def alg51(cube: Cube):
  cube.run_algorithm("Fw (R U R' U') (R U R' U') Fw'")


def alg52(cube: Cube):
  cube.run_algorithm("(R U R' U R Dw') (R U' R' F')")


def alg53(cube: Cube):
  cube.run_algorithm("(Rw' U') (R U') (R' U) (R U') (R' U2 Rw)")


def alg54(cube: Cube):
  cube.run_algorithm("(Rw U) (R' U) (R U') (R' U) (R U2' Rw')")


def alg55(cube: Cube):
  cube.run_algorithm("(R U2) (R2 U' R U' R' U2) (F R F')")


def alg56(cube: Cube):
  cube.run_algorithm("Fw (R U R' U') Fw' F (R U R' U') (R U R' U') F'")


def alg57(cube: Cube):
  cube.run_algorithm("(R U R' U') (M' U R U') Rw'")


class Orientation(Enum):
  """Orientation indicating which way the top color sticker is facing"""

  # Indicates the top color sticker is facing upwards.
  TD = auto()

  # Indicates the top color sticker is facing forwards / backwards.
  FB = auto()

  # Indicates the top color sticker is facing right / left.
  RL = auto()

TD, FB, RL = Orientation.TD, Orientation.FB, Orientation.RL

def get_oll_config(cube: Cube) -> List[Orientation]:
  # Config Order:
  # 0 1 2
  # 3 4 5
  # 6 7 8

  oll_config = []
  top_color = cube.top.center
  # Top row: top left, top middle, top right
  oll_config.append(FB if cube.back.top_right == top_color else RL if cube.left.top_left == top_color else TD)
  oll_config.append(FB if cube.back.top_middle == top_color else TD)
  oll_config.append(FB if cube.back.top_left == top_color else RL if cube.right.top_right == top_color else TD)

  # Middle row: top left, top middle, top right
  oll_config.append(RL if cube.left.top_middle == top_color else TD)
  oll_config.append(TD)
  oll_config.append(RL if cube.right.top_middle == top_color else TD)

  # Bottom row: bottom left, bottom middle, bottom right
  oll_config.append(FB if cube.front.top_left == top_color else RL if cube.left.top_right == top_color else TD)
  oll_config.append(FB if cube.front.top_middle == top_color else TD)
  oll_config.append(FB if cube.front.top_right == top_color else RL if cube.right.top_left == top_color else TD)

  # Quick assertion that all of the TD orientations are in fact correct
  for i in range(len(oll_config)):
    if oll_config[i] == TD:
      assert cube.top.pieces[i] == top_color

  return oll_config


def check_oll_config_matches(oll_config_1: List[Orientation], oll_config_2: List[Orientation]):
  assert len(oll_config_1) == len(oll_config_2)
  return oll_config_1 == oll_config_2


def check_oll_solved(cube: Cube):
  return cube.top.is_solved()


# Detection Algorithm --- Runs OLL casework to determine which algorithm needs to be applied
# Returns whether or not the OLL case was found. If it was, the solution algorithm should be automatically applied to the cube.
def detect_and_run_oll_case(cube: Cube) -> bool:
  # Oll skip case, already solved
  if check_oll_solved(cube):
    return True

  oll_config = get_oll_config(cube)

  # Corners Correct, Edges Flipped --- Possibilities: 28, 57, 20
  if check_oll_config_matches(oll_config, [TD, FB, TD, RL, TD, TD, TD, TD, TD]):
    alg28(cube)
    return True
  elif check_oll_config_matches(oll_config, [TD, FB, TD, TD, TD, TD, TD, FB, TD]):
    alg57(cube)
    return True
  elif check_oll_config_matches(oll_config, [TD, FB, TD, RL, TD, RL, TD, FB, TD]):
    alg20(cube)
    return True

  # All Edges Flipped Correctly --- Possibilities: 23, 24, 25, 27, 26, 22, 21
  if check_oll_config_matches(oll_config, [TD, TD, TD, TD, TD, TD, FB, TD, FB]):
    alg23(cube)
    return True
  elif check_oll_config_matches(oll_config, [TD, TD, FB, TD, TD, TD, TD, TD, FB]):
    alg24(cube)
    return True
  elif check_oll_config_matches(oll_config, [TD, TD, RL, TD, TD, TD, FB, TD, TD]):
    alg25(cube)
    return True
  elif check_oll_config_matches(oll_config, [FB, TD, RL, TD, TD, TD, TD, TD, FB]):
    alg27(cube)
    return True
  elif check_oll_config_matches(oll_config, [RL, TD, TD, TD, TD, TD, FB, TD, RL]):
    alg26(cube)
    return True
  elif check_oll_config_matches(oll_config, [RL, TD, FB, TD, TD, TD, RL, TD, FB]):
    alg22(cube)
    return True
  elif check_oll_config_matches(oll_config, [FB, TD, FB, TD, TD, TD, FB, TD, FB]):
    alg21(cube)
    return True

  # No Edges Flipped Correctly --- Possibilities: 3, 4, 17, 19, 18, 2, 1
  if check_oll_config_matches(oll_config, [FB, FB, RL, RL, TD, RL, RL, FB, TD]):
    alg3(cube)
    return True
  elif check_oll_config_matches(oll_config, [RL, FB, TD, RL, TD, RL, FB, FB, RL]):
    alg4(cube)
    return True
  elif check_oll_config_matches(oll_config, [TD, FB, FB, RL, TD, RL, RL, FB, TD]):
    alg17(cube)
    return True
  elif check_oll_config_matches(oll_config, [TD, FB, TD, RL, TD, RL, RL, FB, RL]):
    alg19(cube)
    return True
  elif check_oll_config_matches(oll_config, [FB, FB, FB, RL, TD, RL, TD, FB, TD]):
    alg18(cube)
    return True
  elif check_oll_config_matches(oll_config, [RL, FB, FB, RL, TD, RL, RL, FB, FB]):
    alg2(cube)
    return True
  elif check_oll_config_matches(oll_config, [RL, FB, RL, RL, TD, RL, RL, FB, RL]):
    alg1(cube)
    return True

  # T shapes --- Possibilities: 33, 45
  if check_oll_config_matches(oll_config, [FB, FB, TD, TD, TD, TD, FB, FB, TD]):
    alg33(cube)
    return True
  elif check_oll_config_matches(oll_config, [RL, FB, TD, TD, TD, TD, RL, FB, TD]):
    alg45(cube)
    return True

  # P shapes --- Possibilities: 44, 43, 32, 31
  if check_oll_config_matches(oll_config, [RL, FB, TD, RL, TD, TD, RL, TD, TD]):
    alg44(cube)
    return True
  elif check_oll_config_matches(oll_config, [TD, FB, RL, TD, TD, RL, TD, TD, RL]):
    alg43(cube)
    return True
  elif check_oll_config_matches(oll_config, [FB, FB, TD, RL, TD, TD, FB, TD, TD]):
    alg32(cube)
    return True
  elif check_oll_config_matches(oll_config, [FB, TD, TD, RL, TD, TD, FB, FB, TD]):
    alg31(cube)
    return True

  # W shapes --- Possibilities: 38, 36
  if check_oll_config_matches(oll_config, [FB, TD, TD, TD, TD, RL, TD, FB, RL]):
    alg38(cube)
    return True
  elif check_oll_config_matches(oll_config, [TD, TD, FB, RL, TD, TD, RL, FB, TD]):
    alg36(cube)
    return True

  # L shapes --- Possibilities: 54, 53, 50, 49, 48, 47
  if check_oll_config_matches(oll_config, [RL, TD, RL, RL, TD, TD, RL, FB, RL]):
    alg54(cube)
    return True
  elif check_oll_config_matches(oll_config, [RL, FB, RL, RL, TD, TD, RL, TD, RL]):
    alg53(cube)
    return True
  elif check_oll_config_matches(oll_config, [RL, FB, FB, RL, TD, TD, RL, TD, FB]):
    alg50(cube)
    return True
  elif check_oll_config_matches(oll_config, [RL, TD, FB, RL, TD, TD, RL, FB, FB]):
    alg49(cube)
    return True
  elif check_oll_config_matches(oll_config, [RL, TD, FB, TD, TD, RL, RL, FB, FB]):
    alg48(cube)
    return True
  elif check_oll_config_matches(oll_config, [FB, TD, RL, RL, TD, TD, FB, FB, RL]):
    alg47(cube)
    return True

  # Big Lightning Bolts --- Possibilities: 39, 40
  if check_oll_config_matches(oll_config, [FB, FB, TD, TD, TD, TD, TD, FB, RL]):
    alg39(cube)
    return True
  elif check_oll_config_matches(oll_config, [TD, FB, FB, TD, TD, TD, RL, FB, TD]):
    alg40(cube)
    return True

  # "C" Shapes --- Possibilities: 34, 46
  if check_oll_config_matches(oll_config, [RL, FB, RL, TD, TD, TD, TD, FB, TD]):
    alg34(cube)
    return True
  elif check_oll_config_matches(oll_config, [TD, TD, RL, RL, TD, RL, TD, TD, RL]):
    alg46(cube)
    return True

  # Squares --- Possibilities: 5, 6
  if check_oll_config_matches(oll_config, [FB, FB, RL, RL, TD, TD, RL, TD, TD]):
    alg5(cube)
    return True
  elif check_oll_config_matches(oll_config, [RL, TD, TD, RL, TD, TD, FB, FB, RL]):
    alg6(cube)
    return True

  # Small Lightning Bolts --- Possibilities: 7, 12, 8, 11
  if check_oll_config_matches(oll_config, [FB, TD, RL, TD, TD, RL, TD, FB, FB]):
    alg7(cube)
    return True
  elif check_oll_config_matches(oll_config, [RL, FB, FB, TD, TD, RL, FB, TD, TD]):
    alg12(cube)
    return True
  elif check_oll_config_matches(oll_config, [TD, FB, FB, TD, TD, RL, FB, TD, RL]):
    alg8(cube)
    return True
  elif check_oll_config_matches(oll_config, [FB, FB, RL, RL, TD, TD, TD, TD, FB]):
    alg11(cube)
    return True

  # Fish Shapes --- Possibilities: 37, 35, 10, 9
  if check_oll_config_matches(oll_config, [TD, TD, RL, TD, TD, RL, FB, FB, TD]):
    alg37(cube)
    return True
  elif check_oll_config_matches(oll_config, [TD, FB, RL, RL, TD, TD, FB, TD, TD]):
    alg35(cube)
    return True
  elif check_oll_config_matches(oll_config, [FB, FB, TD, TD, TD, RL, RL, TD, FB]):
    alg10(cube)
    return True
  elif check_oll_config_matches(oll_config, [RL, TD, FB, TD, TD, RL, FB, FB, TD]):
    alg9(cube)
    return True

  # I Shapes --- Possibilities: 51, 52, 56, 55
  if check_oll_config_matches(oll_config, [RL, FB, FB, TD, TD, TD, RL, FB, FB]):
    alg51(cube)
    return True
  elif check_oll_config_matches(oll_config, [FB, TD, RL, RL, TD, RL, FB, TD, RL]):
    alg52(cube)
    return True
  elif check_oll_config_matches(oll_config, [FB, TD, FB, RL, TD, RL, FB, TD, FB]):
    alg56(cube)
    return True
  elif check_oll_config_matches(oll_config, [RL, TD, RL, RL, TD, RL, RL, TD, RL]):
    alg55(cube)
    return True

  # Knight Move Shapes --- Possibilities: 13, 16, 14, 15
  if check_oll_config_matches(oll_config, [FB, FB, RL, TD, TD, TD, TD, FB, FB]):
    alg13(cube)
    return True
  elif check_oll_config_matches(oll_config, [RL, FB, TD, TD, TD, TD, FB, FB, RL]):
    alg16(cube)
    return True
  elif check_oll_config_matches(oll_config, [RL, FB, FB, TD, TD, TD, FB, FB, TD]):
    alg14(cube)
    return True
  elif check_oll_config_matches(oll_config, [TD, FB, RL, TD, TD, TD, RL, FB, FB]):
    alg15(cube)
    return True

  # Awkward Shapes --- Possibilities: 41, 30, 42, 29
  if check_oll_config_matches(oll_config, [TD, FB, TD, RL, TD, TD, FB, TD, FB]):
    alg41(cube)
    return True
  elif check_oll_config_matches(oll_config, [TD, FB, TD, RL, TD, TD, RL, TD, RL]):
    alg30(cube)
    return True
  elif check_oll_config_matches(oll_config, [TD, FB, TD, TD, TD, RL, FB, TD, FB]):
    alg42(cube)
    return True
  elif check_oll_config_matches(oll_config, [TD, FB, TD, TD, TD, RL, RL, TD, RL]):
    alg29(cube)
    return True

  return False
