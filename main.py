from functools import reduce

# Represents single cell of sudoku
class Cell:
  def __init__(self, value):
    self.value = value

  def set(self, value):
    self.value = value
  
  def has_value(self):
    return self.value != None

  def __str__(self):
    return str(self.value) if self.has_value() else " "

class Row:
  def __init__(self, cells):
    self.cells = cells

  def values(self):
    for cell in self.cells:
      if(cell.has_value()):
        yield cell.value

class Column:
  def __init__(self, cells):
    self.cells = cells

  def values(self):
    for cell in self.cells:
      if(cell.has_value()):
        yield cell.value

class Square:
  def __init__(self, cells):
    self.cells = cells

class Sudoku:
  def __init__(self):
    self.cells=[]
    for _ in range(0, 9):
      row = []
      for _ in range(0, 9):
        cell = Cell(None)
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
    return Column(cells)

  # Returns all columns
  def columns(self):
    for ci in range(0, 9):
      yield self.column(ci)

  # Returns row of specific index (zero based)
  def row(self, index):
    return Row(self.cells[index])

  # Returns all rows
  def rows(self):
    for ri in range(0, 9):
      yield Row(ri)
  
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
sudoku.print()
print(sudoku.number_of_known_values())