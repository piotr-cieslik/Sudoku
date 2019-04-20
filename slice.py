# Represents the 9 element slice of sudoku.
# It can be column, row or 3x3 square.
class Slice:
  def __init__(self, cells):
    self.cells = cells

  def discard_used_values(self):
    values = list(self.values())
    for cell in self.cells:
      cell.discard_values(values)

  # Returns true when value found, returns false otherwise.
  def calculate_value(self):
    for cell in self.cells:
      if(cell.calculate_value(self.cells)):
        return True
    return False

  def valid(self):
    values = [0] * 9
    for cell in self.cells:
      index = cell.value - 1
      if(values[index] == 1):
        return False
      values[index] = 1
    return True

  def values(self):
    for cell in self.cells:
      if(cell.has_value()):
        yield cell.value