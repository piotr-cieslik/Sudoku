import unittest
from cell import Cell

class CellTests(unittest.TestCase):
  def test_clear_possible_when_value_is_set(self):
    cell = Cell()
    cell.set(1)
    self.assertTrue(len(cell._Cell__possible) == 0)

  def test_calculate_value_when_single_possible_value(self):
    cell = Cell()
    cell._Cell__possible == [1]
    result = cell.calculate_value([])
    self.assertTrue(result)
    self.assertEqual(1, cell.value())

  def test_calculate_value_when_multiple_possible_values_and_one_is_unique_in_slice(self):
    cell = Cell()
    cell._Cell__possible = [1, 2, 3]
    other_cell = Cell()
    other_cell._Cell__possible = [1, 2]
    result = cell.calculate_value([other_cell])
    self.assertTrue(result)
    self.assertEqual(3, cell.value())

  def test_not_calculate_value_when_multiple_possible_values_and_none_is_unique_in_slice(self):
    cell = Cell()
    cell._Cell__possible = [1, 2, 3]
    other_cell = Cell()
    other_cell._Cell__possible = [1, 2, 3]
    result = cell.calculate_value([other_cell])
    self.assertFalse(result)
    self.assertEqual(None, cell.value())

if __name__ == '__main__':
    unittest.main()