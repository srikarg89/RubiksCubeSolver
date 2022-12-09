runTest = function(){
    normalCube();
    mixUpString = mixUp();
    solveCube();
    let worked = true;
    for(let j = 0; j < NUM_SIDES; j++){
      for(let k = 0; k < SIDE_LENGTH; k++){
        if(grid[j][k] != grid[j][4]){
          console.log("TEST FAILED");
          console.log(mixUpString);
          worked = false;
        }
      }
    }
    return worked;
}

runTests = function(numIterations){
    for(let i = 0; i < numIterations; i++)
    {
        let worked = runTest();
        if(!worked){
            break;
        }
    }
  }