import unittest
import sys
sys.path.append('.')
from sudoku import Sudoku
from backtracking import Backtracking
from data import Data

class SudokuTests(unittest.TestCase):
  def test_solve_easy(self):
    self.__test_backtracking(Data.easy())

  def test_solve_intermediate(self):
    self.__test_backtracking(Data.intermediate())

  def test_solve_difficult(self):
    self.__test_backtracking(Data.difficult())

  def __test_backtracking(self, data):
    sudoku = Sudoku(data.puzzle)
    Backtracking(sudoku).solve()
    self.assertTrue(self.__are_arrays_equal(data.solution, sudoku.cells))

  def __are_arrays_equal(self, a, b):
    fa = [val for sublist in a for val in sublist]
    fb = [val for sublist in b for val in sublist]
    return fa == fb

if __name__ == '__main__':
    unittest.main()