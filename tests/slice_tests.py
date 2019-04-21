import unittest
import sys
sys.path.append('.')
from cell import Cell
from slice import Slice

class SliceTests(unittest.TestCase):
  def test_valid_when_all_cells_are_filled_and_values_are_unique(self):
    slice = self.__slice(1,2,3,4,5,6,7,8,9)
    self.assertTrue(slice.valid())

  def test_valid_when_not_all_cells_are_filled_and_values_are_unique(self):
    slice = self.__slice(1,2,3,4,5,6,7,8,9)
    self.assertTrue(slice.valid())

  def test_not_valid_when_all_cells_are_filled_and_values_are_not_unique(self):
    slice = self.__slice(1,1,3,4,5,6,7,8,9)
    self.assertFalse(slice.valid())

  def test_it_is_possible_to_iterate_slice_values(self):
    expected = [1,2,3,4,5,6,7,8,9]
    current = []
    for value in self.__slice(*expected):
      current.append(value)
    self.assertTrue(expected == current)
  
  def __slice(self, *values):
    cells = []
    for value in values:
      cell = Cell()
      cell.set(value)
      cells.append(cell)
    return Slice(cells)
    
if __name__ == '__main__':
    unittest.main()