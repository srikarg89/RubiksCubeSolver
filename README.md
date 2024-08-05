# RubiksCubeSolver
A visual representation of the CFOP method to solve the Rubik's Cube made with Python, JavaScript, and [p5.js](https://p5js.org/).

To run the code, first install the requirements using:
```pip install requirements.txt```

Then, begin the Flask server by running `python server.py`. This should display a local URL which you can open up in your browser to see your very own virtual Rubik's Cube!.

In the console (for example in Chrome Devtools) enter one of the following actions to perform that action on the cube.
- `mixUp()`
    - Mix up the cube with a random set of 25 moves, returns the mixup string.
- `solveCube()`
    - Solve the cube from start to finish, returns the solution string.
- `solveCross()`, `solveF2L()`, `solveOll()`, `solvePll()`
    - Solves the individual components of the Rubik's Cube using the CFOP method.
- `makeMove(moves)`
    - Perform individual moves on the Rubik's Cube. The `moves` string can also be a series of moves, in which case the moves should be space-separated.
    - The following moves are permitted: `[R, L, U, D, F, B, x, y, z]`.
    - Each move may also be followed by a `'` (indicating a **prime**, or a turn in the opposite direction) or a `2` (indicating a **double**, or making that move twice in a row).
    - See *solver/base.py* for more details.
