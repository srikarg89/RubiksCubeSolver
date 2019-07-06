//F2L algorithms list
//Function name: f2l + corner position + corner orientation + edge position + edge orientation
//https://drive.google.com/file/d/1nzAXYUWZJ6H2wIOXaHdWXep3W57tArbR/view
/*
f2l1B1F = function(){
  algorithm("");
}
*/
//Corner on top
//Edge on top -- Section 1A
//White on top
f2l1B1F = function(){
  algorithm("U (F R' F' R) U (R U R') ");
}
f2l1B2F = function(){
  algorithm("U2 (R U R') U (R U' R')");
}
f2l1B3F = function(){
  algorithm("U (R U2 R') U (R U' R')");
}
f2l1B4F = function(){
  algorithm("(R U2 R') U' (R U R')");
}
f2l1B1R = function(){
  algorithm("y (L' U2 L) U (L' U' L) y'");
}
f2l1B2R = function(){
  algorithm("y U' (L' U2 L) U' (L' U L) y'");
}
f2l1B3R = function(){
  algorithm("y U2 (L' U' L) U' (L' U L) y'");
}
f2l1B4R = function(){
  algorithm("F (U R U' R') F' (R U' R')");
}
//White on Right
f2l1R1F = function(){
  algorithm("y U L' U2 L U' y' R U R'");
}
f2l1R2F = function(){
  algorithm("U' (R U R') U (R U R')");
}
f2l1R3F = function(){
  algorithm("(R U R')");
}
f2l1R4F = function(){
  algorithm("U' (R U' R') U (R U R')");
}
f2l1F1R = function(){
  algorithm("y U (L' U L) U' (L' U' L) y'");
}
f2l1F2R = function(){
  algorithm("y (L' U' L) y'");
}
f2l1F3R = function(){
  algorithm("y U (L' U' L) U' (L' U' L) y'");
}
f2l1F4R = function(){
  algorithm("U' (R U2 R') U y (L' U' L) y'");
}
//White on front
f2l1F1F = function(){
  algorithm("U (R' F R F') U (R U R')");
}
f2l1F2F = function(){
  algorithm("U' (R U2 R') U2 (R U' R')");
}
f2l1F3F = function(){
  algorithm("U' (R U R') U2 (R U' R')");
}
f2l1F4F = function(){
  algorithm("U (R U' R')");
}
f2l1R1R = function(){
  algorithm("y U' (L' U L) y'");
}
f2l1R2R = function(){
  algorithm("y U (L' U' L) U2 (L' U L) y'");
}
f2l1R3R = function(){
  algorithm("y U (L' U2 L) U2 (L' U L) y'");
}
f2l1R4R = function(){
  algorithm("y F U' F' U2 L' U' L y'");
}

//Edge in slot -- Section 1B Part 1
f2l1B5F = function(){
  algorithm("[R U R' U'][R U R' U'](R U R')");
}
f2l1B5R = function(){
  algorithm("(R U' R') (F' U2 F)");
}
f2l1F5F = function(){
  algorithm("U' R U' R' U2 R U' R'");
}
f2l1F5R = function(){
  algorithm("U' (R U R') U y (L' U' L) y'");
}
f2l1R5F = function(){
  algorithm("U (R U R') U2 (R U R')");
}
f2l1R5R = function(){
  algorithm("U (F' U' F) U' (R U R')");
}

//Edge in wrong slot ----- NEED TO FINISH
//White on top
f2l1B8F = function(){
  algorithm("U' R' U R2 U' R'");
}
f2l1B8R = function(){
  algorithm("y R' F R2 U' R' U2 F' y'");
}
f2l1B6F = function(){
  algorithm("y U L U' L2 U L y'");
}
f2l1B6R = function(){
  algorithm("L F' L2 U L U2 F");
}
f2l1B7F = function(){
  algorithm("y y L2 Uw L2 Uw' L2 y' y'");
}
f2l1B7R = function(){
  algorithm("y y U2 L F' U F L' y' y'");
}
//White on right
f2l1R8F = function(){
  algorithm("R' U' R2 U R'");
}
f2l1R8R = function(){
  algorithm("y L Uw L Uw' L' y'");
}
f2l1R6F = function(){
  algorithm("U' (L' U' L) (R U' R')");
}
f2l1R6R = function(){
  algorithm("(F U2 F') (R U R')");
}
f2l1R7F = function(){
  algorithm("y y U2 U (R U R') (L U L') y' y'");
}
f2l1R7R = function(){
  algorithm("U2 y y y U2 L' B U B' L y");
}
//White on front
f2l1F8F = function(){
  algorithm("y U (R U R') (L' U L) y'");
}
f2l1F8R = function(){
  algorithm("R' U2 R F' U' F");
}
f2l1F6F = function(){
  algorithm("y L U L2' U' L y'");
}
f2l1F6R = function(){
  algorithm("R' Uw' R' Uw R");
}
f2l1F7F = function(){
  algorithm("y y U2 U' R U' R' L U' L' y' y'");
}
f2l1F7R = function(){
  algorithm("y y U2 U2 R B' U' B R' y' y'");
}

//Corner in slot

//Edge on top -- Section 1B Part 2
f2l5B1R = function(){
  algorithm("U (R U' R' U') y (L' U L) y'");
}
f2l5B4F = function(){
  algorithm("U' (R' F R F') (R U R')");
}
f2l5F1R = function(){
  algorithm("y (L' U L) U' (L' U L) y'");
}
f2l5F4F = function(){
  algorithm("(R U R') U' (R U R')");
}
f2l5R1R = function(){
  algorithm("y (L' U' L) U (L' U' L) y'");
}
f2l5R4F = function(){
  algorithm("(R U' R') U (R U' R')");
}

//Edge in slot -- Section 1C
f2l5B5R = function(){
  algorithm("(R U2 R') U (R U2 R') U (F' U' F)");
}
f2l5F5F = function(){
  algorithm("(R U' R') U (R U2 R') U (R U' R')");
}
f2l5F5R = function(){
  algorithm("(R U' R') U2 y (L' U' L) U' (L' U L) y'");
}
f2l5R5F = function(){
  algorithm("(R U' R') U' (R U R') U2 (R U' R')");
}
f2l5R5R = function(){
  algorithm("(Rw U' Rw') U2 (Rw U Rw') (R U R')");
}

//Corner in wrong slot --- Edge on top
//Corner in right slot
f2l8B4R = function(){
  algorithm("y U (R U' R') (L' U L) y'");
}
f2l8B4F = function(){
  algorithm("y y (L' U2 L) U' (L U L') y' y'");
}
f2l8R4R = function(){
  algorithm("y y (L' U' L) U2 (Fw' L' Fw) y' y'");
}
f2l8R4F = function(){
  algorithm("y y U' L' U' L2 U2 L' y' y'");
}
f2l8F4R = function(){
  algorithm("y R (L' U L) R' y'");
}
f2l8F4F = function(){
  algorithm("y y U (L' U L) U (L U L') y' y'");
}
//Corner in left slot
f2l6B1R = function(){
  algorithm("y' (R U2 R') U (R' U' R) y");
}
f2l6B1F = function(){
  algorithm("U' (L' U L) (R U' R')");
}
f2l6R1R = function(){
  algorithm("U (L' U' L) y (L' U' L) y'");
}
f2l6R1F = function(){
  algorithm("L' (R U' R') L");
}
f2l6F1R = function(){
  algorithm("y' U R U R2 U2 R y");
}
f2l6F1F = function(){
  algorithm("y' R U R' U2 Fw R Fw' y");
}
//Corner in back slot
f2l7B2F = function(){
  algorithm("y y y U' (L' U L) y' (L U2 L') y' y'");
}
f2l7B3R = function(){
  algorithm("y y U (R U' R') y (R' U2 R) y");
}
f2l7R2F = function(){
  algorithm("y y (R U' R') (L U2 L') y' y'");
}
f2l7R3R = function(){
  algorithm("y y y (L' U' L) U' (R' U' R) y");
}
f2l7F2F = function(){
  algorithm("y y y (L F' L' F) (R' U2 R) y");
}
f2l7F3R = function(){
  algorithm("y y y (L' U L) (R' U2 R) y");
}

sameArray = function(arr1, arr2){
  return arr1.sort().join(',') === arr2.sort().join(',');
}

findEdge = function(colors){
  switch(colors.sort().join(',')){
    case [grid[0][1],grid[4][7]].sort().join(','):
    return [1,grid[4][7]];
    case [grid[3][1],grid[4][3]].sort().join(','):
    return [2,grid[4][3]];
    case [grid[2][1],grid[4][1]].sort().join(','):
    return [3,grid[4][1]];
    case [grid[1][1],grid[4][5]].sort().join(','):
    return [4,grid[4][5]];
    case [grid[0][5],grid[1][3]].sort().join(','):
    return [5,grid[0][5]];
    case [grid[0][3],grid[3][5]].sort().join(','):
    return [6,grid[0][3]];
    case [grid[3][3],grid[2][5]].sort().join(','):
    return [7,grid[2][5]];
    case [grid[1][5],grid[2][3]].sort().join(','):
    return [8,grid[2][3]];
    case [grid[0][7],grid[5][1]].sort().join(','):
    return [9,grid[5][1]];
    case [grid[3][7],grid[5][3]].sort().join(','):
    return [10,grid[5][3]];
    case [grid[2][7],grid[5][7]].sort().join(','):
    return [11,grid[5][7]];
    case [grid[1][7],grid[5][5]].sort().join(','):
    return [12,grid[5][5]];
    default:
    return null;
  }
}

/*
BY = 1
OY = 2
GY = 3
RY = 4
BR = 5
OB = 6
GO = 7
RG = 8
BW = 9
OW = 10
GW = 11
RW = 12
*/

findCorner = function(colors){
  switch(colors.sort().join(',')){
    case [grid[4][8],grid[0][2],grid[1][0]].sort().join(','):
    return [1,grid[4][8]];
    case [grid[4][6],grid[0][0],grid[3][2]].sort().join(','):
    return [2,grid[4][6]];
    case [grid[4][0],grid[2][2],grid[3][0]].sort().join(','):
    return [3,grid[4][0]];
    case [grid[4][2],grid[2][0],grid[1][2]].sort().join(','):
    return [4,grid[4][2]];
    case [grid[5][2],grid[0][8],grid[1][6]].sort().join(','):
    return [5,grid[5][2]];
    case [grid[5][0],grid[0][6],grid[3][8]].sort().join(','):
    return [6,grid[5][0]];
    case [grid[5][6],grid[2][8],grid[3][6]].sort().join(','):
    return [7,grid[5][6]];
    case [grid[5][8],grid[2][6],grid[1][8]].sort().join(','):
    return [8,grid[5][8]];
    default:
    return null;
  }
}

/*
BYR = 1
BYO = 2
GYO = 3
GYR = 4
BWR = 5
BWO = 6
GWO = 7
GWR = 8
*/
//Solves right f2l case


find1F2LCase = function(){
  let fullAlg = "";
  let corner = [grid[0][4],grid[1][4],grid[5][4]];
  let edge = [grid[0][4],grid[1][4]];
  let [cornerP,tempCO] = findCorner(corner);
  cornerO = "";
  switch(tempCO){
    case grid[5][4]:
    cornerO = "B";
    break;
    case grid[0][4]:
    cornerO = "F";
    break;
    case grid[1][4]:
    cornerO = "R";
    break;
  }
  //Corner on top
  if(cornerP <= 4){
    off = cornerP - 1;
    for(let i = 0; i < off; i++){
      upPrime();
    }
    cornerP = 1;
  }
  let [edgeP,tempEO] = findEdge(edge);
  let edgeO = "";
  switch(tempEO){
    case grid[0][4]:
    edgeO = "F";
    break;
    case grid[1][4]:
    edgeO = "R";
    break;
  }
  if(cornerP <= 4 || edgeP <= 4 || (cornerP == 5 && edgeP <= 5) || (edgeP == 5 && cornerP <= 5)){
    func_string = "f2l" + cornerP + cornerO + edgeP + edgeO;
    if(edgeP <= 4 && cornerP >= 5){
      while(window[func_string] == undefined){
        edgeP = edgeP+1;
        if(edgeP > 4)
          edgeP = 1;
        func_string = "f2l" + cornerP + cornerO + edgeP + edgeO;
        up();
      }
    }
    window[func_string]();
  }
  else{
    if(edgeP == 5){
      right();
      up();
      rightPrime();
    }
    else if(edgeP == 6){
      leftPrime();
      upPrime();
      left();
    }
    else if(edgeP == 7){
      left();
      upPrime();
      leftPrime();
    }
    else if(edgeP == 8){
      rightPrime();
      up();
      right();
    }
    this.find1F2LCase();
  }
}

f2lCaseSolved = function(){
  let fc = grid[0][4];
  let rc = grid[1][4];
  let bc = grid[5][4];
  return (grid[0][5] == fc && grid[1][3] == rc && grid[0][8] == fc && grid[1][6] == rc && grid[5][2] == bc);
}

solveF2L = function(){
  for(let i = 0; i < 4; i++){
    if(!f2lCaseSolved()){
      find1F2LCase();
    }
    turnCubeRight();
  }
}

checkSecondLayer = function(){
  for(let i = 0; i < 4; i++){
    for(let j = 0; j < 6; j++){
      if(grid[i][j+3] != grid[i][4]){
        return false;
      }
    }
  }
  for(let j = 0; j < 9; j++){
    if(grid[5][j] != grid[5][4])
      return false;
  }
  return true;
}
