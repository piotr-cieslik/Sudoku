from functools import reduce
import math

# Represents single cell of sudoku
# Contains specific value or list of possible values.
class Cell:
  def __init__(self):
    self.__value = None
    self.__possible = list(range(1, 10))

  def set(self, value):
    self.__value = value
    self.__possible = []

  # Returns value of cell or None if not set
  def value(self):
    return self.__value
  
  # Set value if not set, and it's only one possible value
  def calculate_value(self):
    if(self.has_value()):
      return
    if(len(self.__possible) == 1):
      self.set(self.__possible[0])

  # Removes values from list of possible values
  def discard_values(self, values):
    for value in values:
      if(value in self.__possible):
        self.__possible.remove(value)
  
  def has_value(self):
    return self.__value != None

  def __str__(self):
    return str(self.__value) if self.has_value() else " "

# Represents the 9 element slice of sudoku.
# It can be column, row or 3x3 square.
class Slice:
  def __init__(self, cells):
    self.__cells = cells

  def discard_used_values(self):
    values = list(self.__values())
    for cell in self.__cells:
      cell.discard_values(values)

  def __values(self):
    for cell in self.__cells:
      if(cell.has_value()):
        yield cell.value()

class Sudoku:
  def __init__(self):
    self.cells=[]
    for _ in range(0, 9):
      row = []
      for _ in range(0, 9):
        cell = Cell()
        row.append(cell)
      self.cells.append(row)

  def set(self, row, column, value):
    self.cells[row][column].set(value)

  def number_of_known_values(self):
    return reduce(
      lambda sum, row: len(list(filter(lambda x: x.has_value(), row))) + sum,
      self.cells,
      0)

  def solve(self):
    while self.number_of_known_values() != 81:
      before = self.number_of_known_values()
      self.__iteration()
      after = self.number_of_known_values()
      if(before == after):
        return False
    return True
  
  def print(self):
    for row in self.cells:
      line = "".join(map(lambda x: str(x), row))
      print("|" + line + "|\n")

  # Single iteration of solve algorithm.
  # Go through each column and discard values from cells.
  # Go through each row and discard values from cells.
  # Go through each square and discard values from cells.
  # Set values in cells with sigle available value.
  def __iteration(self):
    for column in self.__columns():
      column.discard_used_values()
    for row in self.__rows():
      row.discard_used_values()
    for square in self.__squares():
      square.discard_used_values()
    self.__calculate_values()

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

  def __calculate_values(self):
    for row in self.cells:
      for cell in row:
        cell.calculate_value()

class SudokuFromFile:
  def __init__(self, file_name):
    self.file_name = file_name
  
  def load(self):
    sudoku = Sudoku()
    with open(self.file_name) as f:
      rowIndex = 0
      for line in f:
        columnIndex = 0
        for value in line:
          # Convert cell into the number and add it to row
          if(value.isdigit()):
            sudoku.set(rowIndex, columnIndex, int(value))
          if(value.isdigit() or value == " "):
            columnIndex+=1
        # If line contains any value, increment row index
        if(columnIndex != 0):
          rowIndex += 1
    f.close()
    return sudoku

sudoku = SudokuFromFile("sudoku_very_easy.txt").load()
sudoku.solve()
sudoku.print()