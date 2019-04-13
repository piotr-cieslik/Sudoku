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
  
  # Calculates value of the cell.
  # Returns True when value was set or False when not.
  # Algorithm:
  #   - Do nothing when cell value is already set.
  #   - If single available value left, this value will be set as cell value.
  #   - If more than one value is available, check if one of the available values
  #     is unique in slice (column, row, square). If available value is unique,
  #     this value will be set as cell value.
  def calculate_value(self, cells_of_slice):
    if(self.has_value()):
      return
    if(len(self.__possible) == 1):
      self.set(self.__possible[0])
      return True
    for possible in self.__possible:
      unique = True
      for cell_of_slice in cells_of_slice:
        if(self is cell_of_slice):
          continue
        if(possible in cell_of_slice.__possible):
          unique = False
      if(unique):
        self.set(possible)
        return True
    return False

  # Removes values from list of possible values
  def discard_values(self, values):
    for value in values:
      if(value in self.__possible):
        self.__possible.remove(value)
  
  def has_value(self):
    return self.__value != None

  def __str__(self):
    return str(self.__value) if self.has_value() else " "