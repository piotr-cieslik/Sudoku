# Represents single cell of sudoku
class Cell:
  def __init__(self):
    self.value = None
    self.candidates = list(range(1, 10))

  def set(self, value):
    self.value = value
    self.candidates = []

  # Calculates value of the cell in context of current slice.
  # Slice can be row, column or block.
  # Returns True when value was found and set or False when not.
  # Algorithm:
  #   - Do nothing when cell value is already set.
  #   - If single available value left, this value will be set as cell value.
  #   - If more than one value is available, check if one of the available values
  #     is unique in slice (column, row, square). If available value is unique,
  #     this value will be set as cell value.
  def calculate_value(self, cells_of_slice):
    if(self.has_value()):
      return
    if(len(self.candidates) == 1):
      self.set(self.candidates[0])
      return True
    for candidate in self.candidates:
      unique = True
      for cell_of_slice in cells_of_slice:
        if(self is cell_of_slice):
          continue
        if(candidate in cell_of_slice.candidates):
          unique = False
      if(unique):
        self.set(candidate)
        return True
    return False

  # Removes values from list of candidates
  def discard_values(self, values):
    for value in values:
      if(value in self.candidates):
        self.candidates.remove(value)
  
  def has_value(self):
    return self.value != None

  def __str__(self):
    return str(self.value) if self.has_value() else " "