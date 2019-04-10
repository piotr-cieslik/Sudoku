from functools import reduce

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

  # Returns column of specific index (zero based)
  def column(self, index):
    cells = []
    for ri in range(0, 9):
      cells.append(self.cells[ri][index])
    return Slice(cells)

  # Returns all columns
  def columns(self):
    for ci in range(0, 9):
      yield self.column(ci)

  # Returns row of specific index (zero based)
  def row(self, index):
    return Slice(self.cells[index])

  # Returns all rows
  def rows(self):
    for ri in range(0, 9):
      yield self.row(ri)

  def calculate_values(self):
    for row in self.cells:
      for cell in row:
        cell.calculate_value()
  
  def print(self):
    for row in self.cells:
      line = "".join(map(lambda x: str(x), row))
      print("|" + line + "|\n")

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

sudoku = SudokuFromFile("sudoku.txt").load()

for column in sudoku.columns():
  column.discard_used_values()
for row in sudoku.rows():
  row.discard_used_values()

sudoku.calculate_values()

sudoku.print()
print(sudoku.number_of_known_values())