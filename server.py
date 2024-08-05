from flask import Flask, request, jsonify, render_template
from solver.base import Cube
from solver.solve import solve_cross, solve_f2l, solve_oll, solve_pll

app = Flask(__name__)

@app.route("/make_move", methods=["GET"])
def make_move():
    # Process input data
    cube_string = request.args.get('cube_string')
    move = request.args.get('move')

    # Run move
    cube = Cube.from_string(cube_string)
    cube.run_algorithm(move)

    # Return output
    data = {"cube_string": cube.to_string()}
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/mixup", methods=["GET"])
def mixup():
    # Process input data
    cube_string = request.args.get('cube_string')

    # Run move
    cube = Cube.from_string(cube_string)
    cube.mix_up()
    cube.simplify_move_history()

    # Return output
    data = {"cube_string": cube.to_string(), "moves": cube.move_history_as_string()}
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/solve/cross", methods=["GET"])
def solve_cross_endpoint():
    # Process input data
    cube_string = request.args.get('cube_string')

    # Run move
    cube = Cube.from_string(cube_string)
    solve_cross(cube)
    cube.simplify_move_history()

    # Return output
    data = {"cube_string": cube.to_string(), "moves": cube.move_history_as_string()}
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/solve/f2l", methods=["GET"])
def solve_f2l_endpoint():
    # Process input data
    cube_string = request.args.get('cube_string')

    # Run move
    cube = Cube.from_string(cube_string)
    solve_cross(cube)
    solve_f2l(cube)
    cube.simplify_move_history()

    # Return output
    data = {"cube_string": cube.to_string(), "moves": cube.move_history_as_string()}
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/solve/oll", methods=["GET"])
def solve_oll_endpoint():
    # Process input data
    cube_string = request.args.get('cube_string')

    # Run move
    cube = Cube.from_string(cube_string)
    solve_cross(cube)
    solve_f2l(cube)
    solve_oll(cube)
    cube.simplify_move_history()

    # Return output
    data = {"cube_string": cube.to_string(), "moves": cube.move_history_as_string()}
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/solve/pll", methods=["GET"])
def solve_pll_endpoint():
    # Process input data
    cube_string = request.args.get('cube_string')

    # Run move
    cube = Cube.from_string(cube_string)
    solve_cross(cube, minimize_moves=False)
    solve_f2l(cube, minimize_moves=False)
    solve_oll(cube)
    cube._remove_cube_rotations_from_move_history()
    solve_pll(cube)
    cube.simplify_move_history()

    # Return output
    data = {"cube_string": cube.to_string(), "moves": cube.move_history_as_string()}
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)