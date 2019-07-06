# RubiksCubeSolver-JS
A visual representation of F2L to solve the Rubik's Cube made with JavaScript and p5js.

To run the code, simply open the *index.html* file in your browser.

In the console (for example in Chrome Devtools) enter one of the following actions to perform that action on the cube.

- `mixup()`
    - Mix up the cube with a random set of 20 moves, prints out the mixup string.
- `solveCube()`
    - Solve the cube from start to finish, prints out the solution string.
- `solveCross()`, `solveF2L()`, `solveOll()`, `solvePll()`
    - Solve the individual components of the Rubik's Cube.
- `right()`, `rightPrime()`... (find all moves in *moves.js*)
    - Perform individual moves on the Rubik's Cube.