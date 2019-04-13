# Represents the 9 element slice of sudoku.
# It can be column, row or 3x3 square.
class Slice:
  def __init__(self, cells):
    self.__cells = cells

  def discard_used_values(self):
    values = list(self.__values())
    for cell in self.__cells:
      cell.discard_values(values)

  # Returns true when value found, returns false otherwise.
  def calculate_value(self):
    for cell in self.__cells:
      if(cell.calculate_value(self.__cells)):
        return True
    return False

  def __values(self):
    for cell in self.__cells:
      if(cell.has_value()):
        yield cell.value()