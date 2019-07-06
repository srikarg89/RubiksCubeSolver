/* Colors:
	 * 0 = Blue
	 * 1 = Red
	 * 2 = Green
	 * 3 = Orange
	 * 4 = Yellow
	 * 5 = White
	 */

//Grid with cube stuff

let exampleString = "0 4 0 1 0 5 3 3 1 4 4 4 0 1 5 5 3 5 1 4 4 1 2 5 1 2 5 0 0 5 3 3 4 2 5 4 1 0 2 1 4 3 3 2 3 2 0 0 2 5 2 3 1 2";

let count = 0;
let total = 0;

var grid = [];
let size = 30;
var fullString = "";
//Dictionaries relating moves after rotations
var x_dict = {"R":"R", "L":"L", "B":"U", "F":"D", "U":"F", "D":"B"};
var xPrime_dict = {"R":"R", "L":"L", "U":"B", "D":"F", "F":"U", "B":"D"};
var y_dict = {"U":"U", "D":"D", "B":"L", "F":"R", "L":"F", "R":"B"};
var yPrime_dict = {"U":"U", "D":"D", "L":"B", "R":"F", "F":"L", "B":"R"};
var z_dict = {"F":"F", "B":"B", "R":"U", "U":"L", "L":"D", "D":"R"};
var zPrime_dict = {"F":"F", "B":"B", "U":"R", "L":"U", "D":"L", "R":"D"};
let rotationX = 0;
let rotationY = 0;
let rotationStartX = 0;
let rotationStartY = 0;

function setup() {
  createCanvas(900,600,WEBGL);
  rotationX = 0;
  rotationY = 0;
//Makes 2D grid
  for(var x = 0; x < 6; x++){
    let newArr = [];
    for(var y = 0; y < 9; y++){
      newArr.push(null);
    }
    grid.push(newArr);
  }
  //Default cube
//  setCubeFromString(exampleString);
  normalCube();
/*
  for(let i = 0; i < 1000; i++){
    mixUp();
    solveCube();
  }
  console.log(total);
  console.log(count);
  console.log(total/count);
*/
//  mixUp();
//  solveCube();
}

function draw() {
  //Display the background
  background(150);
  //Display the cube
  gridToDisplay(-200);
}

  setCubeFromString = function(input){
    inputArray = input.split(' ');
    for(let i = 0; i < inputArray.length; i++){
      grid[int(i/9)][i%9] = int(inputArray[i]);
    }
  }

  normalCube = function(){
    for (var i = 0; i < grid.length; i++) {
      for (var j = 0; j < grid[i].length; j++) {
        grid[i][j]=i;
      }
    }
  }

  runTests = function(){
    for(let i = 0; i < 100; i++)
    {
      normalCube();
      mixUpString = mixUp();
      solveCube();
      failed = false;
      for(let j = 0; j < grid.length; j++){
        for(let k = 0; k < grid[0].length; k++){
          if(grid[j][k] != grid[j][4]){
            console.log(mixUpString);
            failed = true;
          }
        }
      }
      if(failed){
        break;
      }
    }
  }

  solveCube = function(){
    fullString = "";
    solveCross();
    solveF2L();
    solveOll();
    solvePll();
    let order = fullString.split(" ");
//    console.log(fullString);
    order = getRidOfRotations(order);
    for(let i = 0; i < 5; i++){
      order = refineString(order);
    }
//    console.log(order);
    newFullString = "";
    for(let i = 0; i < order.length; i++){
      newFullString += order[i] + " ";
    }
//    console.log(newFullString);
    let endOfF2L = -1;
    for(let i = 0; i < order.length; i++){
      if(order[i].indexOf("Q") != -1){
//        console.log(i);
        if(order[i] == "Q2"){
          endOfF2L = i;
        }
      }
    }
    total += order.length;
    count++;
    return newFullString;
  }

  getRidOfRotations = function(order){
    let clean = false;
    while(!clean){
      clean = true;
      let index = -1;
      let char = "";
      for(let i = order.length - 1; i >= 0; i--){
        char = order[i].charAt(0);
        if(char == "x" || char == "y" || char == "z"){
          clean = false;
          index = i;
          break;
        }

      }
      if(clean)
        break;

      let dictToUse = {};
      let prime = (order[index].length > 1);
      if(char == "x"){
        dict = x_dict;
        if(prime){
          dict = xPrime_dict;
        }
      }
      else if(char == "y"){
        dict = y_dict;
        if(prime){
          dict = yPrime_dict;
        }
      }
      else if(char == "z"){
        dict = z_dict;
        if(prime){
          dict = zPrime_dict;
        }
      }
      order.splice(index,1);
      for(let i = index; i < order.length; i++){
        let replace = dict[order[i].charAt(0)];
        if(replace != undefined){
          order[i] = replace+order[i].substring(1);
        }
      }
    }
    return order;
  }

  refineString = function(order){
  //Get rid of quads
  for(let i = order.length-1; i >= 0; i--){
    if(order[i] == ""){
      order.splice(i,1);
    }
  }
    for(let i = order.length-5; i >= 0; i--){
      if(order[i] == order[i+1]){
        if(order[i+1] == order[i+2]){
          if(order[i+2] == order[i+3]){
            order.splice(i,4);
          }
        }
      }
    }
    //Combine doubles
    for(let i = order.length-2; i >= 0; i--){
      if(order[i] == order[i+1]+"'" || order[i]+"'" == order[i+1]){
        order.splice(i,2);
      }
    }
    //Switch triple direction
    for(let i = order.length-3; i >= 0; i--){
      if(order[i]==order[i+1] && order[i+1] == order[i+2]){
        order.splice(i+1,2);
        let curr = order[i];
        if(curr.charAt(curr.length-1) == "'"){
          order[i] = curr.substring(0,curr.length-1);
        }
        else{
          order[i] = curr + "'";
        }
      }
    }
    //Find doubles
    for(let i = order.length-2; i >= 0; i--){
      if(order[i] == order[i+1]){
        order.splice(i+1,1);
        if(order[i].charAt(order[i].length-1) == "'"){
          order[i] = order[i].substring(0,order[i].length-1) + "2";
        }
        else if(order[i].charAt(order[i].length-1) == "2"){
          order.splice(i,1);
        }
        else{
          order[i] = order[i] + "2";
        }
      }
    }

    for(let i = order.length-1; i >= 0; i--){
      if((order[i] == "y" || order[i] == "y'") && (order[i+1] == "U" || order[i+1] == "U'")){
        let first = order[i];
        order[i] = order[i+1];
        order[i+1] = first;
      }
    }
    return order;
  }

  setCube = function(){
    grid=[
    [0,3,2,0,0,0,0,0,0],
    [3,2,1,1,1,1,1,1,1],
    [2,0,0,2,2,2,2,2,2],
    [1,1,3,3,3,3,3,3,3],
    [4,4,4,4,4,4,4,4,4],
    [5,5,5,5,5,5,5,5,5]];
  }

  mixUp = function(){
    fullString = "";
    let randomStr = "";
    for(let i = 0; i < 20; i++){
      let rand = parseInt(random(1,12));
      switch(rand){
        case 1:
        randomStr += "R ";
        break;
        case 2:
        randomStr += "R' ";
        break;
        case 3:
        randomStr += "L ";
        break;
        case 4:
        randomStr += "L' ";
        break;
        case 5:
        randomStr += "U ";
        break;
        case 6:
        randomStr += "U' ";
        break;
        case 7:
        randomStr += "D ";
        break;
        case 8:
        randomStr += "D' ";
        break;
        case 9:
        randomStr += "F ";
        break;
        case 10:
        randomStr += "F' ";
        break;
        case 11:
        randomStr += "B ";
        break;
        case 12:
        randomStr += "B' ";
        break;
      }
    }
    console.log(randomStr);
    algorithm(randomStr);
    fullString = "";
    return randomStr;
  }

  gridToDisplay = function(startI){
		for (var i = 0; i < grid.length; i++) {
//      push();
      rectMode(CENTER);
			for (var j = 0; j < grid[i].length; j++) {
					let num = grid[i][j];
          let j1 = j%3;
          let j2 = int(j/3);
          j1--;
          j2--;
          let x = j1*size;
          let y = j2*size;
//          rect(x,y,5,5);
//          console.log(x,y,j,j1);
          drawIt(i,num,x,y);
			}
//      pop();
		}
	}

  function mousePressed(){
    let rotateMouse = map(mouseX,0,width,-3/2*PI,3/2*PI);
    let rotateMouse1 = map(mouseY,0,height,-3/2*PI,3/2*PI);
    rotationStartX = rotateMouse;
    rotationStartY = rotateMouse1;
  }

  function mouseReleased(){
    let rotateMouse = map(mouseX,0,width,-3/2*PI,3/2*PI);
    let rotateMouse1 = map(mouseY,0,height,-3/2*PI,3/2*PI);
    rotationX += (rotateMouse - rotationStartX);
    rotationY += (rotateMouse1 - rotationStartY);
    rotationStartX = 0;
    rotationStartY = 0;
  }

  drawIt = function(side, num, x, y){
    push();
		switch(num){
		case 0:
			fill(0,0,255);
			break;
		case 1:
			fill(255,0,0);
			break;
		case 2:
			fill(0,255,0);
			break;
		case 3:
			fill(255,165,0);
			break;
		case 4:
			fill(255,255,0);
			break;
		case 5:
			fill(255,255,255);
			break;
		}
    let rotateMouse = 0;
    let rotateMouse1 = 0;
    if(mouseIsPressed){
      rotateMouse = map(mouseX,0,width,-3/2*PI,3/2*PI) - rotationStartX;
      rotateMouse1 = map(mouseY,0,height,-3/2*PI,3/2*PI) - rotationStartY;
    }

    rotateY((rotationX + rotateMouse));
    rotateX((rotationY + rotateMouse1));
    rectMode(CENTER);
    switch(side){
      case 0:
      translate(0,0,1.5*size);
      rect(x,y,size,size);
      break;
      case 1:
      rotateY(PI/2);
      translate(0,0,1.5*size);
      rect(x,y,size,size);
      break;
      case 2:
      rotateY(PI);
      translate(0,0,1.5*size);
      rect(x,y,size,size);
      break;
      case 3:
      rotateY(-PI/2);
      translate(0,0,1.5*size);
      rect(x,y,size,size);
      break;
      case 4:
      rotateX(PI/2);
      translate(0,0,1.5*size);
      rect(x,y,size,size);
      break;
      case 5:
      rotateX(-PI/2);
      translate(0,0,1.5*size);
      rect(x,y,size,size);
      break;
    }
    pop();
	}
