# SOURCE: http://www.cubewhiz.com/pll.php

from .base import Cube, check_config_matches, Movement

# Only Corner Stuff

# Aa perm
def aa_perm(cube: Cube):
  cube.run_algorithm("x (R' U R') D2 (R U' R') D2 R2 x'")

# Ab perm
def ab_perm(cube: Cube):
  cube.run_algorithm("x R2 D2 (R U R') D2 (R U' R) x'")

# E perm
def e_perm(cube: Cube):
  cube.run_algorithm("x' (R U') (R' D) (R U R' D') (R U R' D) (R U') (R' D') x")

# Only Edge Stuff

# Ua perm
def ua_perm(cube: Cube):
  cube.run_algorithm("(R U' R U) (R U) (R U') (R' U' R2)")

# Ub perm
def ub_perm(cube: Cube):
  cube.run_algorithm("(R2 U) (R U R' U') (R' U') (R' U R')")

# H perm
def h_perm(cube: Cube):
  cube.run_algorithm("(M2 U) (M2 U2) (M2 U) M2")

# Z perm
def z_perm(cube: Cube):
  cube.run_algorithm("(M2 U) (M2 U) (M' U2) (M2 U2) (M' U2)")

# Swapping two adjacent corners and two edges

# T perm
def t_perm(cube: Cube):
  cube.run_algorithm("R U R' U' R' F R2 U' R' U' R U R' F'")

# F perm
def f_perm(cube: Cube):
  cube.run_algorithm("R' U' F' (R U R' U') (R' F) (R2 U') (R' U' R U) (R' U R)")

# Ja perm
def ja_perm(cube: Cube):
  cube.run_algorithm("R' U L' U2 R U' R' U2 L R U'")

# Jb perm
def jb_perm(cube: Cube):
  cube.run_algorithm("R U R' F' R U R' U' R' F R2 U' R' U'")

# Ra perm
def ra_perm(cube: Cube):
  cube.run_algorithm("R U R' F' R U2 R' U2 R' F R U R U2 R' U'")

# Rb perm
def rb_perm(cube: Cube):
  cube.run_algorithm("R' U2 R U2 R' F R U R' U' R' F' R2 U'")

# Three corners and three edges

# Ga perm
def ga_perm(cube: Cube):
  cube.run_algorithm("(R2 Uw) (R' U R' U' R Uw') R2 y' (R' U R) y")

# Ga perm
def gb_perm(cube: Cube):
  cube.run_algorithm("(R' U' R) y (R2 Uw R' U) (R U' R Uw' R2) y'")

# Ga perm
def gc_perm(cube: Cube):
  cube.run_algorithm("(R2 Uw' R U') (R U R' Uw R2) (Fw R' Fw')")

# Ga perm
def gd_perm(cube: Cube):
  cube.run_algorithm("(R U R') y' (R2 Uw' R U') (R' U R' Uw R2) y")

# Two diagonal corners and two edges

# V perm
def v_perm(cube: Cube):
  cube.run_algorithm("(R' U R' Dw') (R' F' R2 U') (R' U R' F) (R F) y'")

# Na perm
def na_perm(cube: Cube):
  cube.run_algorithm("(z) D (R' U) (R2 D' R D U') (R' U) (R2 D' R U' R) z'")

# Nb perm
def nb_perm(cube: Cube):
  cube.run_algorithm("(z) U' (R D') (R2 U R' D U') (R D') (R2 U R' D R') z'")

# Y perm
def y_perm(cube: Cube):
  cube.run_algorithm("(F R U') (R' U' R U) (R' F') (R U R' U') (R' F R F')")


def check_pll_solved(cube: Cube):
  pll_faces = [cube.front, cube.right, cube.back, cube.left]
  return all(face.is_solved() for face in pll_faces)


# Detection Algorithm --- Runs PLL casework to determine which algorithm needs to be applied
# Returns whether or not the PLL case was found. If it was, the solution algorithm should be automatically applied to the cube.
def detect_and_run_pll_case(cube: Cube) -> bool:
  # Pll skip case, already solved
  if check_pll_solved(cube):
    return True

  # Faces / colors used in PLL detection.
  pll_faces = [cube.front, cube.right, cube.back, cube.left]
  front_color, right_color, back_color, left_color = cube.front.center, cube.right.center, cube.back.center, cube.left.center

  top_pieces = cube.front.top_row + cube.right.top_row + cube.back.top_row + cube.left.top_row
  top_corners = [corner for face in pll_faces for corner in (face.top_left, face.top_right)]
  top_edges = [face.top_middle for face in pll_faces]

  # Corners only --- Possibilities: Aa perm, Ab perm, E perm
  # Check that all of the edges are already in the right spot
  if check_config_matches(top_edges, [front_color, right_color, back_color, left_color]):
    if check_config_matches(top_corners, [front_color, back_color, left_color, front_color, right_color, right_color, back_color, left_color]):
      aa_perm(cube)
      return True
    if check_config_matches(top_corners, [front_color, right_color, back_color, back_color, left_color, front_color, right_color, left_color]):
      ab_perm(cube)
      return True
    if check_config_matches(top_corners, [left_color, right_color, back_color, front_color, right_color, left_color, front_color, back_color]):
      e_perm(cube)
      return True

  # Edges only --- Possibilities: H perm, Z perm, Ua perm, Ub perm
  # Check that all of the corners are already in the right spot
  if check_config_matches(top_corners, [front_color, front_color, right_color, right_color, back_color, back_color, left_color, left_color]):
    if check_config_matches(top_edges, [right_color, left_color, back_color, front_color]):
      ua_perm(cube)
      return True
    if check_config_matches(top_edges, [left_color, front_color, back_color, right_color]):
      ub_perm(cube)
      return True
    if check_config_matches(top_edges, [back_color, left_color, front_color, right_color]):
      h_perm(cube)
      return True
    if check_config_matches(top_edges, [right_color, front_color, left_color, back_color]):
      z_perm(cube)
      return True

  # Swapping Two Adjacent Corners & Two Edges --- Possibilities: Ja perm, Jb perm, T perm, Rb perm, Ra perm, F perm
  # Check that the two right corners need to be swapped.
  if check_config_matches(top_corners, [front_color, right_color, back_color, front_color, right_color, back_color, left_color, left_color]):
    if check_config_matches(top_edges, [front_color, back_color, right_color, left_color]):      
      cube.run_algorithm("U'")
      ja_perm(cube)
      cube.run_algorithm("U")
      return True
    if check_config_matches(top_edges, [right_color, front_color, back_color, left_color]):
      jb_perm(cube)
      return True
    if check_config_matches(top_edges, [front_color, left_color, back_color, right_color]):
      t_perm(cube)
      return True
    if check_config_matches(top_edges, [front_color, right_color, back_color, left_color]):
      ja_perm(cube)
      return True
    if check_config_matches(top_edges, [left_color, right_color, back_color, front_color]):
      cube.run_algorithm("U'")
      rb_perm(cube)
      cube.run_algorithm("U")
      return True
    if check_config_matches(top_edges, [front_color, right_color, left_color, back_color]):
      ra_perm(cube)
      return True
    if check_config_matches(top_edges, [back_color, right_color, front_color, left_color]):
      f_perm(cube)
      return True

  # Cycling Three Corners & Three Edges -- Possibilities: Ga perm, Gb perm, Gc perm, Gd perm
  # These don't really have similarities so just check each one individually.
  if check_config_matches(top_pieces, [left_color, front_color, front_color, right_color, back_color, left_color, front_color, left_color, right_color, back_color, right_color, back_color]):
    ga_perm(cube)
    return True
  if check_config_matches(top_pieces, [right_color, left_color, back_color, left_color, right_color, right_color, back_color, front_color, left_color, front_color, back_color, front_color]):
    gb_perm(cube)
    return True
  if check_config_matches(top_pieces, [right_color, left_color, back_color, left_color, front_color, right_color, back_color, back_color, left_color, front_color, right_color, front_color]):
    gc_perm(cube)
    return True
  if check_config_matches(top_pieces, [left_color, back_color, front_color, right_color, right_color, left_color, front_color, left_color, right_color, back_color, front_color, back_color]):
    gd_perm(cube)
    return True

  # Permutations Of Two Diagonal Corners & Two Edges --- Possibilities: V perm, Na perm, Nb perm, Y perm
  # Check that the bottom right and top left corners need to be swapped, and the bottom left and top right corners are in the right spot.
  if check_config_matches(top_corners, [front_color, back_color, left_color, right_color, back_color, front_color, right_color, left_color]):
    if check_config_matches(top_edges, [front_color, back_color, right_color, left_color]):
      v_perm(cube)
      return True
    elif check_config_matches(top_edges, [back_color, right_color, front_color, left_color]):
      na_perm(cube)
      return True
    elif check_config_matches(top_edges, [front_color, left_color, back_color, right_color]):
      cube.run_algorithm("U")
      nb_perm(cube)
      cube.run_algorithm("U'")
      return True
    elif check_config_matches(top_edges, [front_color, right_color, left_color, back_color]):
      y_perm(cube)
      return True

  # None of the configurations matched, return False
  return False
