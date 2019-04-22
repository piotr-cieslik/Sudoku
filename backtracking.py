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
    (ri, ci) = self.first_empty_cell()
    # Check if next empty cell exist.
    # It's not possible to solve, solved sudoku.
    if(ri == None):
      return False

    for x in self.valid_values_of_cell(ri, ci):
      if(self.__iteration(ri, ci, x)):
        return True
        
    return False

  # Single iteration of algorithm.
  # It sets specified value and check if sudoku is still valid.
  # If yes, it tries to solve value of next empty cell.
  # If no, it leaves cell unset and return false.
  # Parameters:
  #   ri - row index of current cell
  #   ci - column index of current cell
  #   value - value of current cell
  def __iteration(self, ri, ci, value):   
    # Assign value to cell and verify correctness.
    self.sudoku.cells[ri][ci] = value

    # If sudoku is valid, try to solve next value.
    valid =\
      self.sudoku.row(ri).valid() and\
      self.sudoku.column(ci).valid() and\
      self.sudoku.block(ri, ci).valid()
    if(valid):
      (ri_next, ci_next) = self.next_empty_cell(ri, ci)
      # Check if next empty cell exist.
      # If not, returns true.
      if(ri_next == None):
        return True

      for x in self.valid_values_of_cell(ri_next, ci_next):
        if(self.__iteration(ri_next, ci_next, x)):
          return True
    
    # If sudoku is not valid, clear value of the cell and return false.
    self.sudoku.cells[ri][ci] = None
    return False

  # Returns sequence of valid values of the cell.
  # It's algorithm enhancement.
  def valid_values_of_cell(self, ri, ci):
    invalid_values = list(filter(lambda x: x != None,\
      list(self.sudoku.row(ri)) +\
      list(self.sudoku.column(ci)) +\
      list(self.sudoku.block(ri, ci))))
    for value in range(1, 10):
      if(value in invalid_values):
        continue
      yield value

  def first_empty_cell(self):
    if(self.sudoku.cells[0][0] == None):
      return (0, 0)
    return self.next_empty_cell(0, 0)

  def next_empty_cell(self, ri, ci):
    # End of sudoku board.
    if(ri == 8 and ci == 8):
      return (None, None)
    # Calculate position of next cell
    ci_next = ci if ri < 8 else ci + 1
    ri_next = ri + 1 if ri < 8 else 0
    # Check value of next cell.
    # If value is not set, returns position of it.
    if(self.sudoku.cells[ri_next][ci_next] == None):
      return (ri_next, ci_next)
    return self.next_empty_cell(ri_next, ci_next)