function sendRequest(endpoint, inputData, callback){
    // Convert the input data to query parameters
    const queryParams = new URLSearchParams(inputData);
    
    // Construct the URL with query parameters
    const url = `http://localhost:5000${endpoint}?${queryParams}`;

    fetch(url)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json()
    })
    .then(data => {
        callback(data);
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}


function makeMove(move){
    const inputData = {
        cube_string: getCubeString(),
        move: move,
    };

    sendRequest("/make_move", inputData, (data) => {
        console.log("Moves taken: " + data.moves);
        setCubeFromString(data.cube_string);
    });
}

function mixUp(){
    const inputData = {
        cube_string: getCubeString(),
    };

    sendRequest("/mixup", inputData, (data) => {
        console.log("Moves taken to mix up: " + data.moves);
        setCubeFromString(data.cube_string);
    });
}

function solveCross(){
    const inputData = {
        cube_string: getCubeString(),
    };

    sendRequest("/solve/cross", inputData, (data) => {
        console.log("Moves taken to solve cross: " + data.moves);
        setCubeFromString(data.cube_string);
    });
}


function solveF2L(){
    const inputData = {
        cube_string: getCubeString(),
    };

    sendRequest("/solve/f2l", inputData, (data) => {
        console.log("Moves taken to solve F2L: " + data.moves);
        setCubeFromString(data.cube_string);
    });
}


function solveOLL(){
    const inputData = {
        cube_string: getCubeString(),
    };

    sendRequest("/solve/oll", inputData, (data) => {
        console.log("Moves taken to solve OLL: " + data.moves);
        setCubeFromString(data.cube_string);
    });
}


function solvePLL(){
    const inputData = {
        cube_string: getCubeString(),
    };

    sendRequest("/solve/pll", inputData, (data) => {
        console.log("Moves taken to solve PLL: " + data.moves);
        setCubeFromString(data.cube_string);
    });
}
