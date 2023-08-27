# RubiksCubeSolver-JS
A visual representation of F2L to solve the Rubik's Cube made with JavaScript and p5js.

To run the code, simply open the *index.html* file in your browser.

In the console (for example in Chrome Devtools) enter one of the following actions to perform that action on the cube.

- `mixup()`
    - Mix up the cube with a random set of 20 moves, returns the mixup string.
- `solveCube()`
    - Solve the cube from start to finish, returns the solution string.
- `solveCrossJS()`, `solveF2LJS()`, `solveOllJS()`, `solvePllJS()`
    - Solves the individual components of the Rubik's Cube using the CFOP method.
- `right()`, `rightPrime()`... (find all moves in *moves.js*)
    - Perform individual moves on the Rubik's Cube.