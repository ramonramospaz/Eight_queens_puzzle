from eight_queens_puzzle import QueenSolve

def test_solve_queen_problems_1():
    right_result = "row 0-col 0,row 1-col 4,row 2-col 7,row 3-col 5,row 4-col 2,row 5-col 6,row 6-col 1,row 7-col 3,"
    test1=QueenSolve(8)
    result = test1.queenSolution 
    assert result == right_result

def test_solve_queen_problems_2():
    right_result = "row 0-col 0,row 1-col 2,row 2-col 5,row 3-col 7,row 4-col 1,row 5-col 3,row 6-col 8,row 7-col 6,row 8-col 4,"
    test2=QueenSolve(9)
    result = test2.queenSolution 
    assert result == right_result

def test_solve_queen_probles_3():
    right_result = "row 0-col 0,row 1-col 2,row 2-col 5,row 3-col 7,row 4-col 9,row 5-col 4,row 6-col 8,row 7-col 1,row 8-col 3,row 9-col 6,"
    test3=QueenSolve(10)
    result = test3.queenSolution 
    assert result == right_result