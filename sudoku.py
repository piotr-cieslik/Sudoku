import math
from cell import Cell
from slice import Slice

# Pass the array of arrays (9x9) with initial values of sudoku.
# Missing sudoku values should be indicated by None values.
class Sudoku:
  def __init__(self, array):
    self.cells=[]
    for ri in range(0, 9):
      row = []
      for ci in range(0, 9):
        cell = Cell()
        value = array[ri][ci]
        if(value != None):
          cell.set(value)
        row.append(cell)
      self.cells.append(row)

  def solve(self):
    while True:
      new_value_found = self.__iteration()
      if(new_value_found):
        continue
      return

  def values(self):
    values = []
    for ri in range(0, 9):
      values.append([])
      for ci in range(0, 9):
        values[ri].append(self.cells[ri][ci].value)
    return values

  # Single iteration of solve algorithm.
  def __iteration(self):
    for column in self.__columns():
      column.discard_used_values()
    for row in self.__rows():
      row.discard_used_values()
    for square in self.__squares():
      square.discard_used_values()
    for column in self.__columns():
      if(column.calculate_value()):
        return True
    for row in self.__rows():
      if(row.calculate_value()):
        return True
    for square in self.__squares():
      if(square.calculate_value()):
        return True
    return False

  # Returns column of specific index (zero based)
  def __column(self, index):
    cells = []
    for ri in range(0, 9):
      cells.append(self.cells[ri][index])
    return Slice(cells)

  # Returns all columns
  def __columns(self):
    for ci in range(0, 9):
      yield self.__column(ci)

  # Returns row of specific index (zero based)
  def __row(self, index):
    return Slice(self.cells[index])

  # Returns all rows
  def __rows(self):
    for ri in range(0, 9):
      yield self.__row(ri)

  # Return 3x3 square of sudoku.
  # Squares are numbered like
  # 0 | 1 | 2
  # 3 | 4 | 5
  # 6 | 7 | 8
  def __square(self, index):
    row = index % 3
    column = math.floor(index / 3)
    cells = []
    for ri in range(0, 3):
      for ci in range(0,3):
        cells.append(self.cells[row * 3 + ri][column * 3 + ci])
    return Slice(cells)

  def __squares(self):
    for s in range(0, 9):
      yield self.__square(s)
