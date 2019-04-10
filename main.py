class Cell:
  def __init__(self, value):
    self.value = value

  def set(self, value):
    self.value = value
  
  def has_value(self):
    return self.value != None

class Row:
  def __init__(self, cells):
    self.cells = cells

class Column:
  def __init__(self, cells):
    self.cells = cells

class Square:
  def __init__(self, cells):
    self.cells = cells

# Main class that represents sudoku board.
class Board:
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

  # Square represents 3x3 subgrid
  # Each sudoku has 9 squares
  # 1 2 3
  # 4 5 6
  # 7 8 9
  # def square(self, number):

class BoardFromFile:
  def __init__(self, file_name):
    self.file_name = file_name
  
  def load(self):
    board = Board()
    with open(self.file_name) as f:
      rowIndex = 0
      for line in f:
        columnIndex = 0
        for value in line:
          # Convert cell into the number and add it to row
          if(value.isdigit()):
            board.set(rowIndex, columnIndex, int(value))
          if(value.isdigit() or value == " "):
            columnIndex+=1
        # If line contains any value, increment row index
        if(columnIndex != 0):
          rowIndex += 1
    f.close()
    return board

board = BoardFromFile("sudoku.txt").load()
