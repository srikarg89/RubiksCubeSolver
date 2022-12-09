// let exampleString = "0 4 0 1 0 5 3 3 1 4 4 4 0 1 5 5 3 5 1 4 4 1 2 5 1 2 5 0 0 5 3 3 4 2 5 4 1 0 2 1 4 3 3 2 3 2 0 0 2 5 2 3 1 2";
setCubeFromString = function(input){
    inputArray = input.split(' ');
    // assert(inputArray.length == NUM_SIDES * SIDE_LENGTH, "Argument for setCubeFromString should have 64 separated numbers. Input was: " + input);
    inputArray = inputArray.map(x => int(x));
    for(let i = 0; i < NUM_SIDES; i++){
        for(let j = 0; j < SIDE_LENGTH; j++){
        let idx = i * SIDE_LENGTH + j;
        grid[i][j] = inputArray[idx];
        }
    }
}

normalCube = function(){
    setCubeFromString("0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5");
}

solveCube = function(){
  fullString = "";
  solveCross();
  solveF2L();
  solveOll();
  solvePll();

  let order = fullString.split(" ");
  console.log(order);
  order = getRidOfRotations(order);
  console.log(order);
  for(let i = 0; i < 5; i++){
      order = refineString(order);
  }

  return order.join(" ");
}
  

refineString = function(order){
    // Remove empties
    for(let i = order.length-1; i >= 0; i--){
        if(order[i] == ""){
        order.splice(i,1);
        }
    }

    // Get rid of quads
    for(let i = order.length-5; i >= 0; i--){
        if(order[i] == order[i+1] && order[i+1] == order[i+2] && order[i+2] == order[i+3]){
        order.splice(i,4);
        }
    }

    // Combine words that undo themselves
    for(let i = order.length-2; i >= 0; i--){
        if(order[i] == order[i+1] + "'" || order[i] + "'" == order[i+1]){
        order.splice(i,2);
        }
    }

    // Switch triple direction
    for(let i = order.length - 3; i >= 0; i--){
        if(order[i] == order[i+1] && order[i+1] == order[i+2]){
        order.splice(i+1, 2);
        let curr = order[i];
        if(curr.charAt(curr.length-1) == "'"){
            order[i] = curr.substring(0, curr.length-1);
        }
        else{
            order[i] = curr + "'";
        }
        }
    }

    // Find doubles
    for(let i = order.length-2; i >= 0; i--){
        if(order[i] == order[i+1]){
        order.splice(i+1, 1);
        if(order[i].charAt(order[i].length-1) == "2"){
            order.splice(i,1);
        }
        else{
            order[i] = order[i][0] + "2";
        }
        }
    }

    // Always do "y" operations after "U" operations.
    for(let i = order.length - 1; i >= 0; i--){
        if((order[i] == "y" || order[i] == "y'") && (order[i+1] == "U" || order[i+1] == "U'")){
        let first = order[i];
        order[i] = order[i+1];
        order[i+1] = first;
        }
    }
    return order;
}

mixUp = function(){
    fullString = "";
    let randomStr = "";
    let randomMoves = "R R' L L' U U' D D' F F' B B'".split(" ");
    for(let i = 0; i < 25; i++){
        let rand = parseInt(random(1, 12));
        randomStr += randomMoves[rand];
    }
    algorithm(randomStr);
    fullString = "";
    return randomStr;
}

getLastRotationInOrder = function(order){
  for(let i = order.length - 1; i >= 0; i--){
    char = order[i].charAt(0);
    if(char == "x" || char == "y" || char == "z"){
      return [i, order[i]];
    }
  }

  return [null, null];
}

getRidOfRotations = function(order){
  let [index, move] = getLastRotationInOrder(order);
  while(index != null){
      let rotationDicts = {
          "x": x_dict,
          "x'": xPrime_dict,
          "y": y_dict,
          "y'": yPrime_dict,
          "z": z_dict,
          "z'": zPrime_dict,
      };
      let dict = rotationDicts[move];

      order.splice(index,1);
      for(let i = index; i < order.length; i++){
        let replace = dict[order[i].charAt(0)];
        if(replace != undefined){
            order[i] = replace + order[i].substring(1);
        }
      }
      [index, move] = getLastRotationInOrder(order);
    }
  return order;
}




