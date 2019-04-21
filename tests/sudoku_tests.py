import unittest
import sys
sys.path.append('.')
from sudoku import Sudoku
from backtracking import Backtracking
from data import Data

class SudokuTests(unittest.TestCase):
  def test_solve_easy(self):
    data = Data.easy()
    sudoku = Sudoku(data.puzzle)
    Backtracking(sudoku).solve()

    self.assertTrue(self.__are_arrays_equal(data.solution, sudoku.cells))

  def test_solve_intermediate(self):
    data = Data.intermediate()
    sudoku = Sudoku(data.puzzle)
    Backtracking(sudoku).solve()

    self.assertTrue(self.__are_arrays_equal(data.solution, sudoku.cells))

  def test_solve_difficult(self):
    data = Data.difficult()
    sudoku = Sudoku(data.puzzle)
    Backtracking(sudoku).solve()

    self.assertTrue(self.__are_arrays_equal(data.solution, sudoku.cells))

  def __are_arrays_equal(self, a, b):
    fa = [val for sublist in a for val in sublist]
    fb = [val for sublist in b for val in sublist]
    return fa == fb

if __name__ == '__main__':
    unittest.main()