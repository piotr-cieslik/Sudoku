import math

# Pass the array of arrays (9x9) with initial values of sudoku.
# Missing sudoku values should be indicated by None values.
class Sudoku:
  def __init__(self, cells):
    self.cells = cells

  def solve(self):
    for x in range(1, 10):
      if(self.__iteration(0, 0, x)):
        return True

  # Single iteration of solve algorithm.
  def __iteration(self, ri, ci, value):
    ci_next = ci if ri < 8 else ci + 1
    ri_next = ri + 1 if ri < 8 else 0

    if(self.cells[ri][ci] != None):
      return self.__iteration(ri_next, ci_next, value)
    
    self.cells[ri][ci] = value
    row = self.row(ri)
    column = self.column(ci)
    square = self.square(ri, ci)
    valid = self.__valid(row) and self.__valid(column) and self.__valid(square)

    if(valid):
      if(ri == 8 and ci == 8):
        return True
      for x in range(1, 10):
        if(self.__iteration(ri_next, ci_next, x)):
          return True
    
    self.cells[ri][ci] = None
    return False

  # Returns column of specific index (zero based)
  def column(self, index):
    cells = []
    for ri in range(0, 9):
      cells.append(self.cells[ri][index])
    return cells

  # Returns row of specific index (zero based)
  def row(self, index):
    return self.cells[index]

  # Return 3x3 square of sudoku containing cell of specific index
  # ri - row index <1, 9>
  # ci - column index <1, 9>
  def square(self, ri, ci):
    row = math.floor(ri / 3)
    column = math.floor(ci / 3)
    cells = []
    for ri in range(0, 3):
      for ci in range(0,3):
        cells.append(self.cells[row * 3 + ri][column * 3 + ci])
    return cells

  def __valid(self, slice):
    values = [0] * 9
    for cell in slice:
      if(cell == None):
        continue
      index = cell - 1
      if(values[index] == 1):
        return False
      values[index] = 1
    return True