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
    new_value = False
    for ri in range(0, 9):
      for ci in range(0, 9):
        cell = self.cells[ri][ci]
        if(cell.has_value()):
          continue
        row = self.row(ri)
        column = self.column(ci)
        square = self.square(ri, ci)
        cell.discard_values(row.values())
        cell.discard_values(column.values())
        cell.discard_values(square.values())
        if(cell.calculate_value(row.cells)):
          new_value = True
        if(cell.calculate_value(column.cells)):
          new_value = True
        if(cell.calculate_value(square.cells)):
          new_value = True
    return new_value

  # Returns column of specific index (zero based)
  def column(self, index):
    cells = []
    for ri in range(0, 9):
      cells.append(self.cells[ri][index])
    return Slice(cells)

  # Returns row of specific index (zero based)
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