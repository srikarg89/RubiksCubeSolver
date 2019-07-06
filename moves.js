/*
Order of moves:
1) up - Line 15
2) upPrime -
3) down -
4) downPrime -

*/

//Counter clockwise dictionary
let rotateCounterClockwise = {0:1, 1:2, 2:5, 5:8, 8:7, 7:6, 6:3, 3:0}
//Clockwise dictionary
let rotateClockwise = {1:0, 2:1, 5:2, 8:5, 7:8, 6:7, 3:6, 0:3}

up = function(toAppend = true){
  if(toAppend)
    fullString += "U ";
  let temp = [];
  for(var i = 0; i < 3; i++){
    temp.push(grid[0][i]);
  }
  for(var i = 0; i < grid.length; i++){
    if(i < 3){
      for(var j = 0; j < 3; j++){
        grid[i][j] = grid[i+1][j];
      }
    }
    else if(i == 4){
      turn(4,true);
    }
    }
  for(var i = 0; i < 3; i++){
    grid[3][i] = temp[i];
  }
}

upPrime = function(toAppend = true){
  if(toAppend)
    fullString += "U' ";
  let temp = [];
  for(var i = 0; i < 3; i++){
    temp.push(grid[3][i]);
  }
  for(var i = grid.length-1; i >= 0; i--){
    if(i <= 3 & i > 0){
      for(var j = 0; j < 3; j++){
        grid[i][j] = grid[i-1][j];
      }
    }
    else if(i == 4){
      turn(4,false);
    }
    }
  for(var i = 0; i < 3; i++){
    grid[0][i] = temp[i];
  }
}

down = function(toAppend = true){
  if(toAppend)
    fullString += "D ";
  let temp = [];
  for(var i = 6; i < 9; i++){
    temp.push(grid[3][i]);
  }
  for(var i = grid.length-1; i >= 0; i--){
    if(i <= 3 & i > 0){
      for(var j = 6; j < 9; j++){
        grid[i][j] = grid[i-1][j];
      }
    }
    else if(i == 5){
      turn(5,true);
    }
    }
  for(var i = 6; i < 9; i++){
    grid[0][i] = temp[i-6];
  }
}

downPrime = function(toAppend = true){
  if(toAppend)
    fullString += "D' ";
  let temp = [];
  for(var i = 6; i < 9; i++){
    temp.push(grid[0][i]);
  }
  for(var i = 0; i < grid.length; i++){
    if(i < 3){
      for(var j = 6; j < 9; j++){
        grid[i][j] = grid[i+1][j];
      }
    }
    else if(i == 5){
      turn(5,false);
    }
    }
  for(var i = 6; i < 9; i++){
    grid[3][i] = temp[i-6];
  }
}

//RIGHT STUFF

right = function(toAppend = true){
  if(toAppend)
    fullString += "R ";
  let temp = [];
  for(var i = 2; i < 9; i+=3){
    temp.push(grid[5][i]);
  }
  let order = [0,4,2,5];
  for(var k = order.length-1; k > 0; k--){
    let i = order[k];
      for(var j = 2; j < 9; j+= 3){
        let j1 = j;
        let j2 = j;
        if(i == 2){
          j1 = 8-j;
        }
        if(order[k-1] == 2){
          j2 = 8-j;
        }

        grid[i][j1] = grid[order[k-1]][j2];
      }
    }
  turn(1,true);
  for(var i = 2; i < 9; i+=3){
    grid[0][i] = temp[int(i/3)];
  }
}

rightPrime = function(toAppend = true){
  if(toAppend)
    fullString += "R' ";
  let temp = [];
  for(var i = 2; i < 9; i+=3){
    temp.push(grid[0][i]);
  }
  let order = [0,4,2,5];
  for(var k = 0; k < order.length-1; k++){
    let i = order[k];
      for(var j = 2; j < 9; j+= 3){
        let j1 = j;
        let j2 = j;
        if(i == 2){
          j1 = 8-j;
        }
        if(order[k+1] == 2){
          j2 = 8-j;
        }

        grid[i][j1] = grid[order[k+1]][j2];
      }
    }
  turn(1,false);
  for(var i = 2; i < 9; i+=3){
    grid[5][i] = temp[int(i/3)];
  }
}

left = function(toAppend = true){
  if(toAppend)
    fullString += "L ";
  let temp = [];
  for(var i = 0; i < 9; i+=3){
    temp.push(grid[0][i]);
  }
  let order = [0,4,2,5];
  for(var k = 0; k < order.length-1; k++){
    let i = order[k];
      for(var j = 0; j < 9; j+= 3){
        let j1 = j;
        let j2 = j;
        if(i == 2){
          j1 = 8-j;
        }
        if(order[k+1] == 2){
          j2 = 8-j;
        }

        grid[i][j1] = grid[order[k+1]][j2];
      }
    }
  turn(3,true);
  for(var i = 0; i < 9; i+=3){
    grid[5][i] = temp[int(i/3)];
  }
}

leftPrime = function(toAppend = true){
  if(toAppend)
    fullString += "L' ";
  let temp = [];
  for(var i = 0; i < 9; i+=3){
    temp.push(grid[5][i]);
  }
  let order = [0,4,2,5];
  for(var k = order.length-1; k > 0; k--){
    let i = order[k];
      for(var j = 0; j < 9; j+= 3){
        let j1 = j;
        let j2 = j;
        if(i == 2){
          j1 = 8-j;
        }
        if(order[k-1] == 2){
          j2 = 8-j;
        }

        grid[i][j1] = grid[order[k-1]][j2];
      }
    }
  turn(3,false);
  for(var i = 0; i < 9; i+=3){
    grid[0][i] = temp[int(i/3)];
  }
}

//FRONT STUFF

front = function(toAppend = true){
  if(toAppend)
    fullString += "F ";
  turnCubeRight(false);
  right(false);
  turnCubeLeft(false);
}

frontPrime = function(toAppend = true){
  if(toAppend)
    fullString += "F' ";
  turnCubeRight(false);
  rightPrime(false);
  turnCubeLeft(false);
}

back = function(toAppend = true){
  if(toAppend)
    fullString += "B ";
  turnCubeLeft(false);
  right(false);
  turnCubeRight(false);
}

backPrime = function(toAppend = true){
  if(toAppend)
    fullString += "B' ";
  turnCubeLeft(false);
  rightPrime(false);
  turnCubeRight(false);
}

//M Flicks Stuff

middle = function(toAppend = true){
  if(toAppend)
    fullString += "M ";
  right(false);
  leftPrime(false);
  turnCubeDown(false);
}

middlePrime = function(toAppend = true){
  if(toAppend)
    fullString += "M' ";
  rightPrime(false);
  left(false);
  turnCubeUp(false);
}




//Physically rotate the cube

turnCubeRight = function(toAppend = true){
  if(toAppend)
    fullString += "y' ";
  let temp = [];
  for(var i = 0; i < grid[3].length; i++){
    temp.push(grid[3][i]);
  }
  for(var i = 3; i > 0; i--){
    for(var j = 0; j < grid[i].length; j++){
      grid[i][j] = grid[i-1][j];
    }
  }
  for(var i = 0; i < grid[0].length; i++){
    grid[0][i] = temp[i];
  }
  turn(4,false);
  turn(5,true);
}

turnCubeLeft = function(toAppend = true){
  if(toAppend)
    fullString += "y ";
  let temp = [];
  for(var i = 0; i < grid[1].length; i++){
    temp.push(grid[0][i]);
  }
  for(var i = 0; i < 3; i++){
    for(var j = 0; j < grid[i].length; j++){
      grid[i][j] = grid[i+1][j];
    }
  }
  for(var i = 0; i < grid[0].length; i++){
    grid[3][i] = temp[i];
  }
  turn(4,true);
  turn(5,false);
}

turnCubeUp = function(toAppend = true){
  if(toAppend)
    fullString += "x ";
  let temp = [];
  let order = [0,4,2,5];
  for(var i = 0; i < grid[5].length; i++){
    temp.push(grid[5][i]);
  }
  for(var i = 3; i > 0; i--){
    for(var j = 0; j < grid[i].length; j++){
      let j1 = j;
      let j2 = j;
      if(order[i]==2){
        j1 = 8-j;
      }
      if(order[i-1]==2){
        j2 = 8-j;
      }
      grid[order[i]][j1] = grid[order[i-1]][j2];
    }
  }
  for(var i = 0; i < grid[0].length; i++){
    grid[0][i] = temp[i];
  }
  turn(3,false);
  turn(1,true);
}

turnCubeDown = function(toAppend = true){
  if(toAppend)
    fullString += "x' ";
  let temp = [];
  let order = [5,2,4,0];
  for(var i = 0; i < grid[5].length; i++){
    temp.push(grid[0][i]);
  }
  for(var i = 3; i > 0; i--){
    for(var j = 0; j < grid[i].length; j++){
      let j1 = j;
      let j2 = j;
      if(order[i]==2){
        j1 = 8-j;
      }
      if(order[i-1]==2){
        j2 = 8-j;
      }
      grid[order[i]][j1] = grid[order[i-1]][j2];
    }
  }
  for(var i = 0; i < grid[0].length; i++){
    grid[5][i] = temp[i];
  }
  turn(1,false);
  turn(3,true);
}

turnCubeClockwise = function(toAppend = true){
  if(toAppend)
    fullString += "z ";
  let temp = [];
  let order = [4,1,5,3];
  for(var i = 0; i < grid[3].length; i++){
    temp.push(grid[3][i]);
  }
  for(var i = 3; i > 0; i--){
    let first = [2,5,8,1,4,7,0,3,6];
    let second = [];
    for(var j = 0; j < grid[i].length; j++){
      let j1 = j;
      let j2 = j;
      let j3 = 2 - int(j/3);
      j2 = (j%3)*3 + j3;
      grid[order[i]][j2] = grid[order[i-1]][j1];
    }
  }
  for(var i = 0; i < grid[4].length; i++){
    let j2 = 2 - int(i/3);
    let j = (i%3)*3 + j2;
    grid[4][j] = temp[i];
  }
  turn(0,true);
  turn(2,false);
}

turnCubeCounterClockwise = function(toAppend = true){
  if(toAppend)
    fullString += "z' ";
  let temp = [];
  let order = [4,1,5,3];
  for(var i = 0; i < grid[4].length; i++){
    temp.push(grid[4][i]);
  }
  for(var i = 0; i < 3; i++){
    let first = [2,5,8,1,4,7,0,3,6];
    let second = [];
    for(var j = 0; j < grid[i].length; j++){
      let j1 = j;
      let j2 = j;
      let j3 = 2 - int(j/3);
      j2 = (j%3)*3 + j3;
      grid[order[i]][j1] = grid[order[i+1]][j2];
    }
  }
  for(var i = 0; i < grid[3].length; i++){
    let j2 = 2 - int(i/3);
    let j = (i%3)*3 + j2;
    grid[3][i] = temp[j];
  }
  turn(0,false);
  turn(2,true);
}

//Universal turn function
turn = function(i,isClockwise){
  let currNum = 0;
  let count = 0;
  let turnArray;
  if(isClockwise){
    turnArray = rotateClockwise;
  }
  else{
    turnArray = rotateCounterClockwise;
  }
  for(var j = 0; j < 2; j++){
    let temp = grid[i][0];
    currNum = 0;
    count = 0;
    while(0 != turnArray[currNum] && count < 50){
      let currNum1 = turnArray[currNum];
      grid[i][currNum] = grid[i][currNum1];
      currNum = currNum1;
      count += 1;
    }
    grid[i][currNum] = temp;
  }
}

//Finds
algorithm = function(str, toAppend = true){
  for(let i = 0; i < str.length; i++){
    let char = str[i];
    let w = (str[i+1] == "w");
    let nextNum = 1;
    if(w){
      nextNum++;
    }
    let normal = !(str[i+nextNum] == "'");
    let double = (str[i+nextNum] == "2");
    tempAlgorithm(char,w,normal,double, toAppend);
  }
}
//Applies method
tempAlgorithm = function(char,w,normal,double, toAppend){
//  console.log(str);
  for(var i = 0; i < str.length; i++){
    switch(char){
      case 'U':
      if(w){
        if(normal){
          down(toAppend);
          turnCubeLeft(toAppend);
        }else{
          downPrime(toAppend);
          turnCubeRight(toAppend);
        }if(double){
          down(toAppend);
          turnCubeLeft(toAppend);
        }
      }
      else{
        if(normal){up(toAppend);}
        else{upPrime(toAppend);}
        if(double){up(toAppend);}
      }
      break;
      case 'D':
      if(w){
        if(normal){
          up(toAppend);
          turnCubeRight(toAppend);
        } else{
          upPrime(toAppend);
          turnCubeLeft(toAppend);
        }if(double){
          up(toAppend);
          turnCubeRight(toAppend);
        }
      }
      else{
        if(normal){down(toAppend);}
        else{downPrime(toAppend);}
        if(double){down(toAppend);}
      }
      break;
      case 'R':
      if(w){
        if(normal){
          left(toAppend);
          turnCubeUp(toAppend);
        } else{
          leftPrime(toAppend);
          turnCubeDown(toAppend);
        }
        if(double){
          left(toAppend);
          turnCubeUp(toAppend);
        }
      }else{
        if(normal){right(toAppend);}
        else{rightPrime(toAppend);}
        if(double){right(toAppend);}
      }
      break;
      case 'L':
      if(w){
        if(normal){
          right(toAppend);
          turnCubeDown(toAppend);
        } else{
          rightPrime(toAppend);
          turnCubeUp(toAppend);
        }
        if(double){
          right(toAppend);
          turnCubeDown(toAppend);
        }
      }else{
        if(normal){left(toAppend);}
        else{leftPrime(toAppend);}
        if(double){left(toAppend);}
      }
      break;
      case 'F':
      if(w){
        if(normal){
          back(toAppend);
          turnCubeClockwise(toAppend);
        } else{
          backPrime(toAppend);
          turnCubeCounterClockwise(toAppend);
        }
        if(double){
          back(toAppend);
          turnCubeClockwise(toAppend);
        }
      }
      else{
        if(normal){front(toAppend);}
        else{frontPrime(toAppend);}
        if(double){front(toAppend);}
      }
      break;
      case 'B':
      if(w){
        if(normal){
          front(toAppend);
          turnCubeCounterClockwise(toAppend);
        } else{
          frontPrime(toAppend);
          turnCubeClockwise(toAppend);
        }
        if(double){
          front(toAppend);
          turnCubeCounterClockwise(toAppend);
        }
      }
      else{
        if(normal){back(toAppend);}
        else{backPrime(toAppend);}
        if(double){back(toAppend);}
      }
      break;
      case 'M':
      if(normal){middle(toAppend);}
      else{middlePrime(toAppend);}
      if(double){middle(toAppend);}
      break;
      case 'S':
      if(double){frontPrime(toAppend);frontPrime(toAppend);back(toAppend);back(toAppend);turnCubeClockwise(toAppend);turnCubeClockwise(toAppend);}
      else if(normal){frontPrime(toAppend);back(toAppend);turnCubeClockwise(toAppend);}
      else{front(toAppend);backPrime(toAppend);turnCubeCounterClockwise(toAppend);}
      break;
      case 'x':
      if(normal){turnCubeUp(toAppend);}
      else{turnCubeDown(toAppend);}
      if(double){turnCubeUp(toAppend);}
      break;
      case 'y':
      if(normal){turnCubeLeft(toAppend);}
      else{turnCubeRight(toAppend);}
      if(double){turnCubeLeft(toAppend);}
      break;
      case 'z':
      if(normal){turnCubeClockwise(toAppend);}
      else{turnCubeCounterClockwise(toAppend);}
      if(double){turnCubeClockwise(toAppend);}
      break;
    }
    if(!normal){
      i++;
    }

  }

}
