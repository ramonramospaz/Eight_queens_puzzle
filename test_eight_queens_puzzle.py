from eight_queens_puzzle import solve_puzzle

def test_solve_queen_problems_1():
    right_result = ['0', '0', '1', '6', '2', '4', '3', '7', '4', '1', '5', '3', '6', '5', '7', '2']
    result = solve_puzzle(8) 
    assert result == right_result

def test_solve_queen_problems_2():
    right_result = ['0', '0', '1', '2', '2', '5', '3', '7', '4', '1', '5', '3', '6', '8', '7', '6', '8', '4']
    result = solve_puzzle(9)
    assert result == right_result

def test_solve_queen_probles_3():
    right_result = ['0', '0', '1', '2', '2', '5', '3', '7', '4', '9', '5', '4', '6', '8', '7', '1', '8', '3', '9', '6']
    result = solve_puzzle(10)
    assert result == right_result