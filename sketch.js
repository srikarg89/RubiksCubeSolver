/* Colors:
	 * 0 = Blue
	 * 1 = Red
	 * 2 = Green
	 * 3 = Orange
	 * 4 = Yellow
	 * 5 = White
	 */

//Grid with cube stuff

const NUM_SIDES = 6;
const SIDE_LENGTH = 9;

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
  createCanvas(900, 600, WEBGL);
  rotationX = 0;
  rotationY = 0;

  //Makes 2D grid
  grid = new Array(NUM_SIDES).fill(null).map(() => new Array(SIDE_LENGTH).fill(null));

  // Default cube
  normalCube();
}

draw = function() {
  //Display the background and overlay the cube on top
  background(150);
  gridToDisplay(-200);
}

gridToDisplay = function(startI){
  for (var i = 0; i < grid.length; i++) {
    rectMode(CENTER);
    for (var j = 0; j < grid[i].length; j++) {
        let num = grid[i][j];
        let j1 = j%3;
        let j2 = int(j/3);
        j1--;
        j2--;
        let x = j1*size;
        let y = j2*size;
        drawIt(i,num,x,y);
    }
  }
}

mousePressed = function(){
    let rotateMouse = map(mouseX, 0, width, -3/2*PI, 3/2*PI);
    let rotateMouse1 = map(mouseY, 0, height, -3/2*PI, 3/2*PI);
    rotationStartX = rotateMouse;
    rotationStartY = rotateMouse1;
}

mouseReleased = function(){
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
