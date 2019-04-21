import math

# Pass the array of arrays (9x9) with initial values of sudoku.
# Missing sudoku values should be indicated by None values.
class Sudoku:
  def __init__(self, cells):
    self.cells = cells

  # Returns column values of specific index (zero based).
  # Returned array contains 9 numbers.
  # Elements are returned in order from top to bottom.
  def column(self, index):
    cells = []
    for ri in range(0, 9):
      cells.append(self.cells[ri][index])
    return Slice(cells)

  # Returns row values of specific index (zero based).
  # Returned array contains 9 numbers.
  # Elements are returned in order from left to right.
  def row(self, index):
    return Slice(self.cells[index])

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
    return Slice(cells)

class Slice:
  def __init__(self, values):
    self.__values = values

  def valid(self):
    occurences = [0] * 9
    for value in self.__values:
      if(value == None):
        continue
      if(occurences[value - 1] == 1):
        return False
      occurences[value - 1] = 1
    return True