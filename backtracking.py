# Class contains implementation of backtracking algorithm.
# It's brute force approach, that ensures finding a solution, if the solution exists.
# Parameters:
#   sudoku - instance of Sudoku class
class Backtracking:
  def __init__(self, sudoku):
    self.sudoku = sudoku

  # Method tries to solves sudoku.
  # Returns true when solution was found or false otherwise.
  def solve(self):
    for x in range(1, 10):
      if(self.__iteration(0, 0, x)):
        return True
    return False

  # Single iteration of algorithm.
  # It sets specified value and check if sudoku is still valid.
  # If yes, it tries to solve value of next cell.
  # If no, it leaves cell unset and return false.
  # Parameters:
  #   ri - row index of current cell
  #   ci - column index of current cell
  #   value - value of current cell
  def __iteration(self, ri, ci, value):
    # Calculate position of next cell
    ci_next = ci if ri < 8 else ci + 1
    ri_next = ri + 1 if ri < 8 else 0

    # If current cell has value, skip it.
    if(self.sudoku.cells[ri][ci] != None):
      return self.__iteration(ri_next, ci_next, value)
    
    # Assign value to cell and verify correctness.
    self.sudoku.cells[ri][ci] = value

    # If sudoku is valid, try to solve next value.
    if(self.sudoku.row(ri).valid() and self.sudoku.column(ci).valid() and self.sudoku.block(ri, ci).valid()):
      if(ri == 8 and ci == 8):
        return True
      for x in range(1, 10):
        if(self.__iteration(ri_next, ci_next, x)):
          return True
    
    # If sudoku is not valid, clear value of the cell and return false.
    self.sudoku.cells[ri][ci] = None
    return False