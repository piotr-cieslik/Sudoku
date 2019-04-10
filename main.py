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

class Column:
  def __init__(self, cells):
    self.cells = cells

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