// Example string: "0 4 0 1 0 5 3 3 1 4 4 4 0 1 5 5 3 5 1 4 4 1 2 5 1 2 5 0 0 5 3 3 4 2 5 4 1 0 2 1 4 3 3 2 3 2 0 0 2 5 2 3 1 2";
setCubeFromString = function(input){
    inputArray = input.split(' ');
    inputArray = inputArray.map(x => int(x));
    for(let i = 0; i < NUM_SIDES; i++){
        for(let j = 0; j < SIDE_LENGTH; j++){
            let idx = i * SIDE_LENGTH + j;
            grid[i][j] = inputArray[idx];
        }
    }
}

getCubeString = function(){
    let cube_string = "";
    for(let i = 0; i < NUM_SIDES; i++){
        for(let j = 0; j < SIDE_LENGTH; j++){
            if(i == 0 && j == 0){
                cube_string += grid[i][j];
            }
            else{
                cube_string += " " + grid[i][j];
            }
        }
    }
    return cube_string;
}

normalCube = function(){
    setCubeFromString("0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5");
}  

mixUp = function(){
    let randomStr = "";
    let randomMoves = "R R' L L' U U' D D' F F' B B'".split(" ");
    for(let i = 0; i < 25; i++){
        let rand = parseInt(random(1, 12));
        randomStr += randomMoves[rand];
    }
    algorithm(randomStr);
    return randomStr;
}
