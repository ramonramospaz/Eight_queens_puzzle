#!/usr/bin/python3

from __future__ import print_function
import sys
from databaseQueensPuzzle import check_database_exist,insert_result_queens_puzzle,show_results_queens_puzzle

class QueenSolve:
  def __init__(self,size):
    self.size=size
    self.queenSolution=""
    self.solve()

  def solve(self):
    check_database_exist()
    positions = [-1] * self.size
    self.put_queen(positions, 0)

  def put_queen(self, positions, target_row):
    if self.queenSolution == "":
      if target_row == self.size:
        self.show_solution(positions)
      else:
        for column in range(self.size):
          if self.check_place(positions, target_row, column):
            positions[target_row] = column
            self.put_queen(positions, target_row + 1)

  def check_place(self, positions, ocuppied_rows, column):
    for i in range(ocuppied_rows):
      if positions[i] == column or \
        positions[i] - i == column - ocuppied_rows or \
        positions[i] + i == column + ocuppied_rows:
        return False
    return True

  def show_solution(self, positions):
    for row in range(self.size):
      for column in range(self.size):
        if positions[row] == column:
          self.queenSolution+=f"row {row}-col {column},"
    print("-----------------------")
    print(self.queenSolution)
    print("-----------------------")
    insert_result_queens_puzzle(self.size,self.queenSolution)

if __name__ == '__main__':
  # By default, solve the 8x8 problem.
  board_size = 8
  if len(sys.argv) > 1:
    board_size = int(sys.argv[1])

  if board_size < 8 and board_size >= 0:
    board_size = 8
    print("Change size of the table to 8")
  
  if board_size > 0:
    print("The result is:")
    #solve_puzzle(board_size)
    QueenSolve(board_size)
  elif board_size == -1:
    show_results_queens_puzzle()