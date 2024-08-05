import random
from typing import List, Optional
from enum import Enum, auto, IntEnum
from dataclasses import dataclass, field


class Color(IntEnum):
    BLUE = 0
    RED = 1
    GREEN = 2
    ORANGE = 3
    YELLOW = 4
    WHITE = 5


class Movement(Enum):
    # Regular moves
    UP = auto()
    DOWN = auto()
    RIGHT = auto()
    LEFT = auto()
    FRONT = auto()
    BACK = auto()

    # Cube rotations
    YAW_CUBE_CW = auto()
    PITCH_CUBE_CW = auto()
    ROLL_CUBE_CW = auto()

    # W moves
    UP_W = auto()
    DOWN_W = auto()
    RIGHT_W = auto()
    LEFT_W = auto()
    FRONT_W = auto()
    BACK_W = auto()

    # Flicks
    M_FLICK = auto()
    E_FLICK = auto()
    S_FLICK = auto()


MOVEMENT_MAPPING = {
    # Normal movements
    "U": Movement.UP,
    "D": Movement.DOWN,
    "R": Movement.RIGHT,
    "L": Movement.LEFT,
    "F": Movement.FRONT,
    "B": Movement.BACK,

    # Rotational movements
    "x": Movement.PITCH_CUBE_CW,
    "y": Movement.YAW_CUBE_CW,
    "z": Movement.ROLL_CUBE_CW,

    # w movements
    "Uw": Movement.UP_W,
    "Dw": Movement.DOWN_W,
    "Rw": Movement.RIGHT_W,
    "Lw": Movement.LEFT_W,
    "Fw": Movement.FRONT_W,
    "Bw": Movement.BACK_W,

    # Flick movements
    "M": Movement.M_FLICK,
    "E": Movement.E_FLICK,
    "S": Movement.S_FLICK,
}

INV_MOVEMENT_MAPPING = {value: key for key, value in MOVEMENT_MAPPING.items()}

class Direction(Enum):
    CW = auto()
    CCW = auto()


@dataclass
class Face:
    # Piece Order:
    # 0 1 2
    # 3 4 5
    # 6 7 8
    pieces: List[Color]

    def __post_init__(self):
        assert len(self.pieces) == 9

    def copy(self):
        return Face(self.pieces.copy())

    @staticmethod
    def fill(color: Color) -> "Face":
        return Face([color for _ in range(9)])

    def flip_vertical(self):
        self.pieces = self.pieces[6:9] + self.pieces[3:6] + self.pieces[0:3]

    def flip_horizontal(self):
        top_row = self.pieces[0:3][::-1]
        middle_row = self.pieces[3:6][::-1]
        bottom_row = self.pieces[6:9][::-1]
        self.pieces = top_row + middle_row + bottom_row

    # Row shortcuts

    @property
    def top_row(self) -> List[Color]:
        return self.pieces[0:3]

    @top_row.setter
    def top_row(self, row: List[Color]):
        assert len(row) == 3
        self.pieces[0:3] = row

    @property
    def middle_row(self) -> List[Color]:
        return self.pieces[3:6]

    @middle_row.setter
    def middle_row(self, row: List[Color]):
        assert len(row) == 3
        self.pieces[3:6] = row

    @property
    def bottom_row(self) -> List[Color]:
        return self.pieces[6:9]

    @bottom_row.setter
    def bottom_row(self, row: List[Color]):
        assert len(row) == 3
        self.pieces[6:9] = row

    # Column shortcuts

    @property
    def left_col(self) -> List[Color]:
        return self.pieces[0::3]

    @left_col.setter
    def left_col(self, col: List[Color]):
        assert len(col) == 3
        self.pieces[0::3] = col

    @property
    def middle_col(self) -> List[Color]:
        return self.pieces[1::3]

    @middle_col.setter
    def middle_col(self, col: List[Color]):
        assert len(col) == 3
        self.pieces[1::3] = col

    @property
    def right_col(self) -> List[Color]:
        return self.pieces[2::3]

    @right_col.setter
    def right_col(self, col: List[Color]):
        assert len(col) == 3
        self.pieces[2::3] = col

    # Individual piece shortcuts

    @property
    def top_left(self) -> Color:
        return self.pieces[0]

    @property
    def top_middle(self) -> Color:
        return self.pieces[1]

    @property
    def top_right(self) -> Color:
        return self.pieces[2]

    @property
    def middle_left(self) -> Color:
        return self.pieces[3]

    @property
    def center(self) -> Color:
        return self.pieces[4]

    @property
    def middle_right(self) -> Color:
        return self.pieces[5]

    @property
    def bottom_left(self) -> Color:
        return self.pieces[6]

    @property
    def bottom_middle(self) -> Color:
        return self.pieces[7]

    @property
    def bottom_right(self) -> Color:
        return self.pieces[8]

    def is_solved(self) -> bool:
        return all([c == self.center for c in self.pieces])

    def _get_pieces_by_index(self, arr: List[int]):
        return [self.pieces[idx] for idx in arr]

    def rotate_clockwise(self):
        """Rotate the face stickers in the clockwise direction"""
        # 0 1 2          6 3 0
        # 3 4 5   --->   7 4 1
        # 6 7 8          8 5 2
        self.pieces = self._get_pieces_by_index([6, 3, 0, 7, 4, 1, 8, 5, 2])

    def rotate_counterclockwise(self):
        """Rotate the face stickers in the counter clockwise direction"""
        # 0 1 2          2 5 8
        # 3 4 5   --->   1 4 7
        # 6 7 8          0 3 6
        self.pieces = self._get_pieces_by_index([2, 5, 8, 1, 4, 7, 0, 3, 6])


def cycle_array_reverse(arr: List):
    """Cycles an array in reverse, so [F, L, B, R] cycled once would be [R, F, L, B]"""
    return arr[-1:] + arr[:-1]


@dataclass
class Cube:
    front: Face
    right: Face
    back: Face
    left: Face
    top: Face
    bottom: Face

    moves_history: List[Movement] = field(default_factory=list)

    @staticmethod
    def default() -> "Cube":
        return Cube(
            front = Face.fill(Color.BLUE),
            right = Face.fill(Color.RED),
            back = Face.fill(Color.GREEN),
            left = Face.fill(Color.ORANGE),
            top = Face.fill(Color.YELLOW),
            bottom = Face.fill(Color.WHITE),
        )

    @staticmethod
    def from_string(string: str) -> "Cube":
        """Converts a cube string to a Cube object. Strings are used to communicate between JS and Python"""
        arr = [int(i) for i in string.strip().split()]
        assert len(arr) == 54

        # String order is front, right, back, left, top, bottom
        front = Face([Color(num) for num in arr[0:9]])
        right = Face([Color(num) for num in arr[9:18]])
        back = Face([Color(num) for num in arr[18:27]])
        left = Face([Color(num) for num in arr[27:36]])
        top = Face([Color(num) for num in arr[36:45]])
        bottom = Face([Color(num) for num in arr[45:54]])
        return Cube(
            front=front, right=right, back=back, left=left, top=top, bottom=bottom
        )

    def to_string(self) -> str:
        """Converts the Cube object to a cube string. Strings are used to communicate between JS and Python"""
        # String order is front, right, back, left, top, bottom
        arr: List[int] = []
        arr.extend(int(c) for c in self.front.pieces)
        arr.extend(int(c) for c in self.right.pieces)
        arr.extend(int(c) for c in self.back.pieces)
        arr.extend(int(c) for c in self.left.pieces)
        arr.extend(int(c) for c in self.top.pieces)
        arr.extend(int(c) for c in self.bottom.pieces)
        return " ".join([str(i) for i in arr])

    def copy(self):
        return Cube(
            front=self.front.copy(),
            right=self.right.copy(),
            back=self.back.copy(),
            left=self.left.copy(),
            top=self.top.copy(),
            bottom=self.bottom.copy(),
            moves_history=self.moves_history.copy(),
        )

    def run_movement(self, movement: Movement, add_to_history=True):
        # Regular movements
        if movement == Movement.UP:
            # Top face rotates CW, top row moves F -> L -> B -> R -> F
            self.top.rotate_clockwise()
            top_rows = [
                self.front.top_row,
                self.left.top_row,
                self.back.top_row,
                self.right.top_row,
            ]
            cycled_top_rows = cycle_array_reverse(top_rows)
            (
                self.front.top_row,
                self.left.top_row,
                self.back.top_row,
                self.right.top_row,
            ) = cycled_top_rows
        elif movement == Movement.DOWN:
            # Bottom face rotates CW, bottom row moves F -> R -> B -> L -> F
            self.bottom.rotate_clockwise()
            bottom_rows = [
                self.front.bottom_row,
                self.right.bottom_row,
                self.back.bottom_row,
                self.left.bottom_row,
            ]
            cycled_bottom_rows = cycle_array_reverse(bottom_rows)
            (
                self.front.bottom_row,
                self.right.bottom_row,
                self.back.bottom_row,
                self.left.bottom_row,
            ) = cycled_bottom_rows
        elif movement == Movement.RIGHT:
            # Right face rotates CW, right col moves F -> U -> B -> D -> F
            # The RIGHT rotation involves the front, top, and bottom faces's right col, and the back face's left col.
            #   Also, the back face's left col is in reverse.
            self.right.rotate_clockwise()
            cols = [
                self.front.right_col,
                self.top.right_col,
                self.back.left_col,
                self.bottom.right_col,
            ]
            cycled_cols = cycle_array_reverse(cols)
            self.front.right_col = cycled_cols[0]
            self.top.right_col = cycled_cols[1]
            self.back.left_col = cycled_cols[2][::-1]
            self.bottom.right_col = cycled_cols[3][::-1]
        elif movement == Movement.LEFT:
            # Left face rotates CW, left col moves F -> D -> B -> U -> F
            # The LEFT rotation involves the front, top, and bottom faces's left col, and the back face's right col.
            #   Also, the back face's right col is in reverse.
            self.left.rotate_clockwise()
            cols = [
                self.front.left_col,
                self.bottom.left_col,
                self.back.right_col,
                self.top.left_col,
            ]
            cycled_cols = cycle_array_reverse(cols)
            self.front.left_col = cycled_cols[0]
            self.bottom.left_col = cycled_cols[1]
            self.back.right_col = cycled_cols[2][::-1]
            self.top.left_col = cycled_cols[3][::-1]
        elif movement == Movement.FRONT:
            # Front face rotates CW, goes from left face's right col -> top face's bottom row -> right face's left col -> bottom face's top row -> left face's right col.
            # The left face's right col and the bottom face's top row are reversed in comparison to the right face's left col and the top face's bottom row.
            self.front.rotate_clockwise()
            cols_and_rows = [
                self.left.right_col,
                self.top.bottom_row,
                self.right.left_col,
                self.bottom.top_row,
            ]
            cycled_cols_and_rows = cycle_array_reverse(cols_and_rows)
            self.left.right_col = cycled_cols_and_rows[0]
            self.top.bottom_row = cycled_cols_and_rows[1][::-1]
            self.right.left_col = cycled_cols_and_rows[2]
            self.bottom.top_row = cycled_cols_and_rows[3][::-1]
        elif movement == Movement.BACK:
            # Back face rotates CW, goes from left face's left col -> bottom face's bottom row -> right face's right col -> top face's top row -> left face's left col.
            # The left face's right col and the bottom face's top row are reversed in comparison to the right face's left col and the top face's bottom row.
            self.back.rotate_clockwise()
            cols_and_rows = [
                self.left.left_col,
                self.bottom.bottom_row,
                self.right.right_col,
                self.top.top_row,
            ]
            cycled_cols_and_rows = cycle_array_reverse(cols_and_rows)
            self.left.left_col = cycled_cols_and_rows[0][::-1]
            self.bottom.bottom_row = cycled_cols_and_rows[1]
            self.right.right_col = cycled_cols_and_rows[2][::-1]
            self.top.top_row = cycled_cols_and_rows[3]
        # Cube rotations
        elif movement == Movement.PITCH_CUBE_CW:
            self.right.rotate_clockwise()
            self.left.rotate_counterclockwise()
            face_order = [self.front, self.top, self.back, self.bottom]
            cycled_faces = cycle_array_reverse(face_order)
            self.front = cycled_faces[0]
            self.top = cycled_faces[1]
            self.back = cycled_faces[2]
            self.back.flip_vertical()
            self.back.flip_horizontal()
            self.bottom = cycled_faces[3]
            self.bottom.flip_vertical()
            self.bottom.flip_horizontal()
        elif movement == Movement.YAW_CUBE_CW:
            self.top.rotate_clockwise()
            self.bottom.rotate_counterclockwise()
            face_order = [self.front, self.left, self.back, self.right]
            self.front, self.left, self.back, self.right = cycle_array_reverse(
                face_order
            )
        elif movement == Movement.ROLL_CUBE_CW:
            self.front.rotate_clockwise()
            self.back.rotate_counterclockwise()
            face_order = [self.top, self.right, self.bottom, self.left]
            self.top, self.right, self.bottom, self.left = cycle_array_reverse(face_order)

            # Fix face orientations
            self.top.rotate_clockwise()
            self.right.rotate_clockwise()
            self.bottom.rotate_clockwise()
            self.left.rotate_clockwise()
        # W movements
        elif movement == Movement.UP_W:
            self.run_movement(Movement.YAW_CUBE_CW, add_to_history=add_to_history)
            self.run_movement(Movement.DOWN, add_to_history=add_to_history)
            add_to_history = False
        elif movement == Movement.DOWN_W:
            self.run_movement(Movement.YAW_CUBE_CW, add_to_history=add_to_history)
            self.run_movement(Movement.YAW_CUBE_CW, add_to_history=add_to_history)
            self.run_movement(Movement.YAW_CUBE_CW, add_to_history=add_to_history)
            self.run_movement(Movement.UP, add_to_history=add_to_history)
            add_to_history = False
        elif movement == Movement.RIGHT_W:
            self.run_movement(Movement.PITCH_CUBE_CW, add_to_history=add_to_history)
            self.run_movement(Movement.LEFT, add_to_history=add_to_history)
            add_to_history = False
        elif movement == Movement.LEFT_W:
            self.run_movement(Movement.PITCH_CUBE_CW, add_to_history=add_to_history)
            self.run_movement(Movement.PITCH_CUBE_CW, add_to_history=add_to_history)
            self.run_movement(Movement.PITCH_CUBE_CW, add_to_history=add_to_history)
            self.run_movement(Movement.RIGHT, add_to_history=add_to_history)
            add_to_history = False
        elif movement == Movement.FRONT_W:
            self.run_movement(Movement.ROLL_CUBE_CW, add_to_history=add_to_history)
            self.run_movement(Movement.BACK, add_to_history=add_to_history)
            add_to_history = False
        elif movement == Movement.BACK_W:
            self.run_movement(Movement.ROLL_CUBE_CW, add_to_history=add_to_history)
            self.run_movement(Movement.ROLL_CUBE_CW, add_to_history=add_to_history)
            self.run_movement(Movement.ROLL_CUBE_CW, add_to_history=add_to_history)
            self.run_movement(Movement.FRONT, add_to_history=add_to_history)
            add_to_history = False
        elif movement == Movement.M_FLICK:
            # M = x' R L'
            self.run_movement(Movement.PITCH_CUBE_CW, add_to_history=add_to_history)
            self.run_movement(Movement.PITCH_CUBE_CW, add_to_history=add_to_history)
            self.run_movement(Movement.PITCH_CUBE_CW, add_to_history=add_to_history)
            self.run_movement(Movement.RIGHT, add_to_history=add_to_history)
            self.run_movement(Movement.LEFT, add_to_history=add_to_history)
            self.run_movement(Movement.LEFT, add_to_history=add_to_history)
            self.run_movement(Movement.LEFT, add_to_history=add_to_history)
            add_to_history = False
        elif movement == Movement.E_FLICK:
            # E = y' U D'
            self.run_movement(Movement.YAW_CUBE_CW, add_to_history=add_to_history)
            self.run_movement(Movement.YAW_CUBE_CW, add_to_history=add_to_history)
            self.run_movement(Movement.YAW_CUBE_CW, add_to_history=add_to_history)
            self.run_movement(Movement.UP, add_to_history=add_to_history)
            self.run_movement(Movement.DOWN, add_to_history=add_to_history)
            self.run_movement(Movement.DOWN, add_to_history=add_to_history)
            self.run_movement(Movement.DOWN, add_to_history=add_to_history)
            add_to_history = False
        elif movement == Movement.S_FLICK:
            # S = z F' B
            self.run_movement(Movement.ROLL_CUBE_CW, add_to_history=add_to_history)
            self.run_movement(Movement.FRONT, add_to_history=add_to_history)
            self.run_movement(Movement.FRONT, add_to_history=add_to_history)
            self.run_movement(Movement.FRONT, add_to_history=add_to_history)
            self.run_movement(Movement.BACK, add_to_history=add_to_history)
            add_to_history = False
        # Unknown movement, throw ValueError
        else:
            raise ValueError(f"Unknown movement {movement} was specified")

        if add_to_history:
            self.moves_history.append(movement)

    def run_algorithm(self, algorithm: str):
        # Remove any ( or ) from the move string
        algorithm = algorithm.replace("(", " ")
        algorithm = algorithm.replace(")", " ")
        moves = algorithm.strip().split()
        for move in moves:
            move = move.strip()
            key = move[0]
            if len(move) > 1 and move[1] == "w":
                key = move[:2]
            assert (
                key in MOVEMENT_MAPPING
            ), f"Unknown move {move} was passed into run_algorithm, full algorithm string was {algorithm}"
            movement = MOVEMENT_MAPPING[key]
            if move.endswith("2'") or move.endswith("2"):
                # Double move case
                self.run_movement(movement)
                self.run_movement(movement)
            elif move.endswith("'"):
                # Prime case
                self.run_movement(movement)
                self.run_movement(movement)
                self.run_movement(movement)
            else:
                # Normal case
                self.run_movement(movement)

    def reset_history(self):
        self.moves_history = []

    def reset(self):
        self.front = Face([Color.BLUE for _ in range(9)])
        self.right = Face([Color.RED for _ in range(9)])
        self.back = Face([Color.GREEN for _ in range(9)])
        self.left = Face([Color.ORANGE for _ in range(9)])
        self.top = Face([Color.YELLOW for _ in range(9)])
        self.bottom = Face([Color.WHITE for _ in range(9)])
        self.reset_history()

    def num_turns_in_move_history(self) -> int:
        string = self.move_history_as_string()
        return sum(2 if move[-1] == "2" else 1 for move in string.split())

    def move_history_as_string(self) -> str:
        # Remove quads from move history
        self._remove_quads_from_move_history()

        # Convert tripes into primes and doubles into double moves.
        simplified_moves_history = []
        idx = 0
        while idx < len(self.moves_history):
            move_base_char = INV_MOVEMENT_MAPPING[self.moves_history[idx]]
            # Convert triples into primes
            if (
                idx + 2 < len(self.moves_history)
                and self.moves_history[idx]
                == self.moves_history[idx + 1]
                == self.moves_history[idx + 2]
            ):
                simplified_moves_history.append(move_base_char + "'")
                idx += 3
            # Convert doubles into twos
            elif (
                idx + 1 < len(self.moves_history)
                and self.moves_history[idx] == self.moves_history[idx + 1]
            ):
                simplified_moves_history.append(move_base_char + "2")
                idx += 2
            else:
                simplified_moves_history.append(move_base_char)
                idx += 1

        return " ".join(simplified_moves_history)

    def _get_last_rotation(self) -> Optional[int]:
        # Reverse the list to find the last index rather than the first index.
        rev_moves = self.moves_history[::-1]
        rev_indices = [
            rev_moves.index(move)
            for move in [
                Movement.PITCH_CUBE_CW,
                Movement.YAW_CUBE_CW,
                Movement.ROLL_CUBE_CW,
            ]
            if move in rev_moves
        ]

        # Return the index of the last rotation in the move history, or None if there are no rotations in the move history.
        if len(rev_indices) == 0:
            return None
        return len(self.moves_history) - min(rev_indices) - 1

    def remove_cube_rotations_from_move_history(self):
        # Dictionaries mapping moves with cube rotations to identical moves without the cube rotations. pitch = x, yaw = y, roll = z.
        reversed_rotations = []
        R, L, U, D, F, B = (
            Movement.RIGHT,
            Movement.LEFT,
            Movement.UP,
            Movement.DOWN,
            Movement.FRONT,
            Movement.BACK,
        )
        pitch_dict = {R: R, L: L, B: U, F: D, U: F, D: B}
        yaw_dict = {U: U, D: D, B: L, F: R, L: F, R: B}
        roll_dict = {F: F, B: B, R: U, U: L, L: D, D: R}
        movement_to_dict_mapping = {
            Movement.PITCH_CUBE_CW: pitch_dict,
            Movement.YAW_CUBE_CW: yaw_dict,
            Movement.ROLL_CUBE_CW: roll_dict,
        }

        # In each loop cycle, find the last cube rotation, and alter the following moves so that the cube rotation can be deleted.
        last_rotation_idx = self._get_last_rotation()
        while last_rotation_idx is not None:
            rotation = self.moves_history[last_rotation_idx]
            reversed_rotations.append(rotation)
            rotation_dict = movement_to_dict_mapping[rotation]

            # Apply the corresponding dict changes only to the moves that occur after the rotation.
            before_rotation = self.moves_history[:last_rotation_idx]
            after_rotation = [
                rotation_dict[move]
                for move in self.moves_history[last_rotation_idx + 1:]
            ]
            self.moves_history = before_rotation + after_rotation
            last_rotation_idx = self._get_last_rotation()

        # Undo all the rotations so that the cube is facing the same as the original way.
        for rotation in reversed_rotations:
            self.run_movement(rotation, add_to_history=False)
            self.run_movement(rotation, add_to_history=False)
            self.run_movement(rotation, add_to_history=False)


    def _remove_quads_from_move_history(self):
        quads_removed = []

        # Cancel out quads. That is, B L F R R R R F -> B L F F
        idx = 0
        while idx < len(self.moves_history):
            if (
                idx < len(self.moves_history) - 3 and
                self.moves_history[idx]
                == self.moves_history[idx + 1]
                == self.moves_history[idx + 2]
                == self.moves_history[idx + 3]
            ):
                # Skip all 4 moves, and don't add any of them to the quads_removed list.
                idx += 4
            else:
                # Add the move normally to the quads_removed list.
                quads_removed.append(self.moves_history[idx])
                idx += 1

        self.moves_history = quads_removed

    def simplify_move_history(self):
        self.remove_cube_rotations_from_move_history()
        self._remove_quads_from_move_history()

    def mix_up(self, num_moves=25) -> "Cube":
        random_move_choices = [Movement.UP, Movement.DOWN, Movement.FRONT, Movement.BACK, Movement.RIGHT, Movement.LEFT]
        for _ in range(num_moves):
            move = random.choice(random_move_choices)
            self.run_movement(move)


def check_config_matches(current: List[Color], config: List[Color]) -> bool:
    """Checks that two lists of colors match, with Nones being ignored"""
    assert len(current) == len(config)
    return all(
        config_val is None or curr_val == config_val
        for curr_val, config_val in zip(current, config)
    )


def realign_cube(cube: Cube, front_color: Color):
    if front_color == cube.front.center:
        return
    if front_color == cube.right.center:
        cube.run_movement(Movement.YAW_CUBE_CW)
        return
    if front_color == cube.back.center:
        cube.run_movement(Movement.YAW_CUBE_CW)
        cube.run_movement(Movement.YAW_CUBE_CW)
        return
    if front_color == cube.left.center:
        cube.run_movement(Movement.YAW_CUBE_CW)
        cube.run_movement(Movement.YAW_CUBE_CW)
        cube.run_movement(Movement.YAW_CUBE_CW)
        return
    raise ValueError(f"Front color {front_color} is not one of the four front-back / right-left colors")
