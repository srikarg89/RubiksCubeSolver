from flask import Flask, request, jsonify, render_template
from solver.base import Cube, get_randomly_mixed_up_cube
from solver.cross import check_cross_solved
from solver.f2l import check_f2l_solved
from solver.oll import check_oll_solved
# from solver.solve import solve_cross, check_cross_solved, check_f2l_solved, check_oll_solved, check_pll_solved, check_cube_solved
from solver.solve import solve_cross, solve_f2l, solve_oll, solve_pll, check_cube_solved

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
    print(data)
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
    print(data)
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/test/cross", methods=["GET"])
def test_cross_endpoint():
    # Process input data
    num_tests = int(request.args.get('num_tests'))

    # Run move
    fails = []
    for _ in range(num_tests):
        cube = get_randomly_mixed_up_cube()
        cube_string = cube.to_string()
        solve_cross(cube)
        if not check_cross_solved(cube):
            fails.append(cube_string)

    # Return output
    data = {"Success rate": (num_tests - len(fails)) / num_tests, "Fails": fails}
    print(data)
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
    print(data)
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/test/f2l", methods=["GET"])
def test_f2l_endpoint():
    # Process input data
    num_tests = int(request.args.get('num_tests'))

    # Run move
    fails = []
    for _ in range(num_tests):
        cube = get_randomly_mixed_up_cube()
        cube_string = cube.to_string()
        solve_cross(cube, minimize_moves=False)
        solve_f2l(cube)
        cube._remove_cube_rotations_from_move_history()
        if not check_f2l_solved(cube):
            fails.append(cube_string)

    # Return output
    data = {"Success rate": (num_tests - len(fails)) / num_tests, "Fails": fails}
    print(data)
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
    print(data)
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/test/oll", methods=["GET"])
def test_oll_endpoint():
    # Process input data
    num_tests = int(request.args.get('num_tests'))

    # Run move
    fails = []
    for _ in range(num_tests):
        cube = get_randomly_mixed_up_cube()
        cube_string = cube.to_string()
        solve_cross(cube, minimize_moves=False)
        solve_f2l(cube, minimize_moves=False)
        solve_oll(cube)
        cube._remove_cube_rotations_from_move_history()
        if not check_oll_solved(cube):
            fails.append(cube_string)
            break

    # Return output
    data = {"Success rate": (num_tests - len(fails)) / num_tests, "Fails": fails}
    print(data)
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
    print(data)
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/test/pll", methods=["GET"])
def test_pll_endpoint():
    # Process input data
    num_tests = int(request.args.get('num_tests'))

    # Run move
    fails = []
    for _ in range(num_tests):
        cube = get_randomly_mixed_up_cube()
        cube_string = cube.to_string()
        solve_cross(cube)
        solve_f2l(cube)
        solve_oll(cube)
        cube._remove_cube_rotations_from_move_history()
        solve_pll(cube)
        cube._remove_cube_rotations_from_move_history()
        if not check_cube_solved(cube):
            fails.append(cube_string)

    # Return output
    data = {"Success rate": (num_tests - len(fails)) / num_tests, "Fails": fails}
    print(data)
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)