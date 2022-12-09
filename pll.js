//SOURCE: http://www.cubewhiz.com/pll.php

//Only Corner Stuff

//Aa perm
aAPerm = function(){
  algorithm("x (R' U R') D2 (R U' R') D2 R2 x'");
}

//Ab perm
aBPerm = function(){
  algorithm("x R2 D2 (R U R') D2 (R U' R) x'");
}

//E perm
ePerm = function(){
  algorithm("x' (R U') (R' D) (R U R' D') (R U R' D) (R U') (R' D') x");
}

//Only Edge Stuff

//Ua perm
uAPerm = function(){
  algorithm("(R U' R U) (R U) (R U') (R' U' R2)");
}

//Ub perm
uBPerm = function(){
  algorithm("(R2 U) (R U R' U') (R' U') (R' U R')");
}

//H perm
hPerm = function(){
  algorithm("(M2 U) (M2 U2) (M2 U) M2");
}

//Z perm
zPerm = function(){
  algorithm("(M2 U) (M2 U) (M' U2) (M2 U2) (M' U2)");
}

//Swapping two adjacent corners and two edges

//T perm
tPerm = function(){
  algorithm("R U R' U' R' F R2 U' R' U' R U R' F'");
}

//F perm
fPerm = function(){
  algorithm("R' U' F'");
  tPerm();
  front();
  up();
  right();
}

//Ja perm
jAPerm = function(){
  algorithm("R' U L' U2 R U' R' U2 L R U'");
}

//Jb perm
jBPerm = function(){
  algorithm("R U R' F' R U R' U' R' F R2 U' R' U'");
}

//Ra perm
rAPerm = function(){
  algorithm("R U R' F' R U2 R' U2 R' F R U R U2 R' U'");
}

//Rb perm
rBPerm = function(){
  algorithm("R' U2 R U2 R' F R U R' U' R' F' R2 U'");
}

//Three corners and three edges

//Ga perm
gAPerm = function(){
  algorithm("(R2 Uw) (R' U R' U' R Uw') R2 y' (R' U R) y");
}

//Ga perm
gBPerm = function(){
  algorithm("(R' U' R) y (R2 Uw R' U) (R U' R Uw' R2) y'");
}

//Ga perm
gCPerm = function(){
  algorithm("	(R2 Uw' R U') (R U R' Uw R2) (Fw R' Fw')");
}

//Ga perm
gDPerm = function(){
  algorithm("	(R U R') y' (R2 Uw' R U') (R' U R' Uw R2) y");
}

//Two diagonal corners and two edges

//V perm
vPerm = function(){
  algorithm("(R' U R' Dw') (R' F' R2 U') (R' U R' F) (R F) y'");
}

//Na perm
nAPerm = function(){
  algorithm("(z) D (R' U) (R2 D' R D U') (R' U) (R2 D' R U' R) z'");
}

//Nb perm
nBPerm = function(){
  algorithm("	(z) U' (R D') (R2 U R' D U') (R D') (R2 U R' D R') z'");
}

//Y perm
yPerm = function(){
  algorithm("	(F R U') (R' U' R U) (R' F') (R U R' U') (R' F R F')");
}


//Detection Algorithm
findCase = function(){
  let topPieces = [];
  for(var i = 0; i < 4; i++){
    for(var j = 0; j < 3; j++){
      topPieces.push(grid[i][j]);
    }
  }

  //Colors
  let curr = grid[0][4];
  let right = grid[1][4];
  let opposite = grid[2][4];
  let left = grid[3][4];

  //Pll skip case, already solved
  if(topPieces[0] == curr && topPieces[1] == curr && topPieces[2] == curr && topPieces[3] == right && topPieces[4] == right && topPieces[5] == right && topPieces[6] == opposite && topPieces[7] == opposite && topPieces[8] == opposite && topPieces[9] == left && topPieces[10] == left && topPieces[11] == left)
    return true;

  //Diagonal corners --- Possibilities: V perm, Na perm, Nb perm, Y perm
  if(topPieces[0] == curr && topPieces[2] == opposite && topPieces[3] == left && topPieces[5] == right && topPieces[6] == opposite && topPieces[8] == curr && topPieces[9] == right && topPieces[11] == left){
    //V perm
    if(topPieces[4] == opposite && topPieces[7] == right){
      vPerm();
      return true;
    }
    //Nb perm
    else if(topPieces[1] == opposite && topPieces[7] == curr){
      nAPerm();
      return true;
    }
    //Na perm
    else if(topPieces[4] == left && topPieces[10] == right){
      up();
      nBPerm();
      upPrime();
      return true;
    }
    //Y perm
    else if(topPieces[7] == left && topPieces[10] == opposite){
      yPerm();
      return true;
    }
  }

  //Adjacent corners --- Possibilities: Ja perm, Jb perm, T perm, Rb perm, Ra perm, F perm
  if(topPieces[0] == curr && topPieces[2] == right && topPieces[3] == opposite && topPieces[5] == curr && topPieces[6] == right && topPieces[8] == opposite && topPieces[9] == left && topPieces[11] == left){
    //F perm
    if(topPieces[1] == opposite && topPieces[4] == right && topPieces[7] == curr && topPieces[10] == left){
      fPerm();
      return true;
    }
    //T perm
    else if(topPieces[1] == curr && topPieces[4] == left && topPieces[7] == opposite && topPieces[10] == right){
      tPerm();
      return true;
    }
    //Jb perm
    else if(topPieces[1] == right && topPieces[4] == curr && topPieces[7] == opposite && topPieces[10] == left){
      jBPerm();
      return true;
    }

    //Ra perm
    else if(topPieces[1] == curr && topPieces[4] == right && topPieces[7] == left && topPieces[10] == opposite){
      rAPerm();
      return true;
    }
    //Need to turn for these
    //Rb perm
    else if(topPieces[1] == left && topPieces[4] == right && topPieces[7] == opposite && topPieces[10] == curr){
      upPrime();
      rBPerm();
      up();
      return true;
    }
    //Ja perm
    else if(topPieces[1] == curr && topPieces[4] == opposite && topPieces[7] == right && topPieces[10] == left){
      upPrime();
      jAPerm();
      up();
      return true;
    }
  }

  //Edges only --- Possibilities: H perm, Z perm, Ua perm, Ub perm
  if(topPieces[0] == curr && topPieces[2] == curr && topPieces[3] == right && topPieces[5] == right && topPieces[6] == opposite && topPieces[8] == opposite && topPieces[9] == left && topPieces[11] == left){
    //H perm
    if(topPieces[1] == opposite && topPieces[4] == left && topPieces[7] == curr && topPieces[10] == right){
      hPerm();
      return true;
    }
    //Z perm
    if(topPieces[1] == right && topPieces[4] == curr && topPieces[7] == left && topPieces[10] == opposite){
      zPerm();
      return true;
    }
    //Ua perm
    if(topPieces[1] == right && topPieces[4] == left && topPieces[7] == opposite && topPieces[10] == curr){
      uAPerm();
      return true;
    }
    //Ub perm
    if(topPieces[1] == left && topPieces[4] == curr && topPieces[7] == opposite && topPieces[10] == right){
      uBPerm();
      return true;
    }
  }

  //Corners only --- Possibilities: Aa perm, Ab perm, E perm
  if(topPieces[1] == curr && topPieces[4] == right && topPieces[7] == opposite && topPieces[10] == left){

    //Aa perm
    if(topPieces[0] == curr && topPieces[2] == opposite && topPieces[3] == left && topPieces[5] == curr && topPieces[6] == right && topPieces[8] == right && topPieces[9] == opposite && topPieces[11] == left){
      aAPerm();
      return true;
    }

    //Ab perm
    if(topPieces[0] == curr && topPieces[2] == right && topPieces[3] == opposite && topPieces[5] == opposite && topPieces[6] == left && topPieces[8] == curr && topPieces[9] == right && topPieces[11] == left){
      aBPerm();
      return true;
    }
    //E perm
    if(topPieces[0] == left && topPieces[2] == right && topPieces[3] == opposite && topPieces[5] == curr && topPieces[6] == right && topPieces[8] == left && topPieces[9] == curr && topPieces[11] == opposite){
      ePerm();
      return true;
    }
  }

  //Three corners and three edges -- Possibilities: Ga perm, Gb perm
  if(topPieces[1] == curr && topPieces[2] == curr && topPieces[3] == right){
    //Ga perm
    if(topPieces[0] == left && topPieces[4] == opposite && topPieces[5] == left && topPieces[6] == curr && topPieces[7] == left && topPieces[8] == right && topPieces[9] == opposite && topPieces[10] == right && topPieces[11] == opposite){
      gAPerm();
      return true;
    }
    //Gb perm
    if(topPieces[0] == opposite && topPieces[4] == left && topPieces[5] == opposite && topPieces[6] == left && topPieces[7] == right && topPieces[8] == left && topPieces[9] == curr && topPieces[10] == opposite && topPieces[11] == right){
      upPrime();
      gBPerm();
      up();
      return true;
    }
  }
  //Continuation of three corners and three edges -- Possibilities: Gc perm, Gd perm
  if(topPieces[5] == right && topPieces[6] == opposite && topPieces[7] == opposite){
    //Gc perm
    if(topPieces[0] == right && topPieces[1] == left && topPieces[2] == opposite && topPieces[3] == left && topPieces[4] == curr && topPieces[8] == left && topPieces[9] == curr && topPieces[10] == right && topPieces[11] == curr){
      gCPerm();
      return true;
    }
    //Gd perm
    if(topPieces[0] == left && topPieces[1] == right && topPieces[2] == left && topPieces[3] == curr && topPieces[4] == left && topPieces[8] == curr && topPieces[9] == right && topPieces[10] == curr && topPieces[11] == opposite){
      up();
      gDPerm();
      upPrime();
      return true;
    }
    return false;
  }
}

solvePll = function(){
  outer: for(var i = 0; i < 4; i++){
    up();
    for(var j = 0; j < 4; j++){
      if(findCase()){
        break outer;
      }
      turnCubeRight();
    }
  }
}

getAllFunctions = function(){
  var allfunctions=[];
  for (var i in window) {
    if((typeof window[i]).toString()=="function"){
      allfunctions.push(window[i].name);
    }
  }
}
