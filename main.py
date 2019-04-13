from sudoku import Sudoku

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

sudoku = SudokuFromFile("sudoku_hard.txt").load()
sudoku.solve()
sudoku.print()