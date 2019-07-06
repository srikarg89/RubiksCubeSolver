//let solveCount = 0;
//let bottomColor = grid[5][4];

checkFinishedCross = function(){
  let bottomColor = grid[5][4];
  if(grid[5][1] != bottomColor || grid[5][3] != bottomColor || grid[5][5] != bottomColor || grid[5][7] != bottomColor){
    return false;
  }
  for(let i = 0; i < 4; i++){
    if(grid[i][4] != grid[i][7]){
      return false;
    }
  }
  return true;
}

findPosition = function(otherColor){
  for(let i = 0; i < 4; i++){
    if(grid[i][4] == otherColor){
      return i;
    }
  }
  return -1;
}

insert = function(algString, position){
  for(let i = 0; i < position; i++){
    downPrime();
  }
  algorithm(algString);
  for(let i = 0; i < position; i++){
    down();
  }
}

crossCases = function(){
  let bottomColor = grid[5][4];
  //6 cases:
  //1. piece is on the top side
  //2. piece is on the top edge
  //3. piece is on the left edge
  //4. piece is on the right edge
  //5. piece is on the bottom edge
  //6. piece is on the bottom but in the wrong spot

  //Case 1
  if(grid[4][7] == bottomColor){
    let otherColor = grid[0][1];
    let position = findPosition(otherColor);
    insert("F2",position);
    return true;
  }
  //Case 2
  if(grid[0][1] == bottomColor){
    let otherColor = grid[4][7];
    let position = findPosition(otherColor);
    let index = 0;
    while(grid[5][1] == bottomColor){ //Opens up the bottom edge
      down();
      index++;
    }
    front();
    for(let i = 0; i < index; i++){ //Returns to previous orientation
      downPrime();
    }
    position += 3;
    position %= 4;
    insert("R'",position);
    return true;
  }
  //Case 3
  if(grid[0][3] == bottomColor){
    let otherColor = grid[3][5];
    let position = findPosition(otherColor);
    position += 1;
    position %= 4;
    insert("L",position);
    return true;
  }
  //Case 4
  if(grid[0][5] == bottomColor){
    let otherColor = grid[1][3];
    let position = findPosition(otherColor);
    position += 3;
    position %= 4;
    insert("R'",position);
    return true;
  }
  //Case 5 - NEED TO FINISH
  if(grid[0][7] == bottomColor){
    let otherColor = grid[5][1];
    let position = findPosition(otherColor);
    front();
    position += 3;
    position %= 4;
    insert("R'",position);
    return true;
  }
  //Case 6
  if(grid[5][1] == bottomColor && grid[0][7] != grid[0][4]){
    let otherColor = grid[0][7];
    let position = findPosition(otherColor);
    front();
    insert("F'",position);
    return true;
  }
  return false;
}

solveCross = function(){
  while(!checkFinishedCross()){
    if(!crossCases()){
      turnCubeRight();
    }
  }
}
