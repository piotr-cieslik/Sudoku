import unittest
from sudoku import Sudoku

# Sudokus taken from https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html
class SudokuTest(unittest.TestCase):
  def test_solve_easy(self):
    _ = None
    missing = [
      [_, _, _, 2, 6, _, 7, _, 1],
      [6, 8, _, _, 7, _, _, 9, _],
      [1, 9, _, _, _, 4, 5, _, _],
      [8, 2, _, 1, _, _, _, 4, _],
      [_, _, 4, 6, _, 2, 9, _, _],
      [_, 5, _, _, _, 3, _, 2, 8],
      [_, _, 9, 3, _, _, _, 7, 4],
      [_, 4, _, _, 5, _, _, 3, 6],
      [7, _, 3, _, 1, 8, _, _, _],
    ]
    expected = [
      [4, 3, 5, 2, 6, 9, 7, 8, 1],
      [6, 8, 2, 5, 7, 1, 4, 9, 3],
      [1, 9, 7, 8, 3, 4, 5, 6, 2],
      [8, 2, 6, 1, 9, 5, 3, 4, 7],
      [3, 7, 4, 6, 8, 2, 9, 1, 5],
      [9, 5, 1, 7, 4, 3, 6, 2, 8],
      [5, 1, 9, 3, 2, 6, 8, 7, 4],
      [2, 4, 8, 9, 5, 7, 1, 3, 6],
      [7, 6, 3, 4, 1, 8, 2, 5, 9],
    ]

    sudoku = Sudoku(missing)
    sudoku.solve()
    actual = sudoku.values()

    self.assertTrue(self.__are_arrays_equal(expected, actual))

  def __are_arrays_equal(self, a, b):
    fa = [val for sublist in a for val in sublist]
    fb = [val for sublist in b for val in sublist]
    return fa == fb

if __name__ == '__main__':
    unittest.main()