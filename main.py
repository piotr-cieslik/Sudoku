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

sudokuAsText = "\
2 3|5  |   \n\
4  |9  | 5 \n\
 25|   |  1\n\
---|---|---\n\
   |   |   \n\
   |   |   \n\
   |   |   \n\
---|---|---\n\
   |   |   \n\
   |   |   \n\
   |   |   \n"

board = Board()
rowIndex = 0
for row in sudokuAsText.splitlines():
  # Skip cells containing separator
  if(row[0] == "-"):
    continue
  # New row
  columnIndex = 0
  for value in row:
    # Skip cells containing separator
    if(value == "|"):
      continue
    # Convert cell into the number and add it to row
    if(value != " "):
      board.set(rowIndex, columnIndex, int(value))
    columnIndex+=1
  rowIndex += 1