import unittest
# We will define sum_array in sum_array.py later
from sum_array import sum_array

class TestSumArray(unittest.TestCase):

    def test_empty_array(self):
        # Test case 1: Empty array
        numbers = []
        self.assertEqual(sum_array(numbers), 0)

    def test_single_element_array(self):
        # Test case 2: Single element array
        numbers = [21]
        self.assertEqual(sum_array(numbers), 21)

    def test_multiple_elements_array(self):
        # Test case 3: Multiple elements array
        numbers = [1, 2, 3, 4]
        self.assertEqual(sum_array(numbers), 10)

    def test_negative_numbers(self):
        # Test case 4: Negative numbers
        numbers = [-1, -2, 5]
        self.assertEqual(sum_array(numbers), 2)

    def test_mixed_numbers(self):
        # Test case 5: Mixed positive, negative, and zero
        numbers = [10, -5, 0, 2]
        self.assertEqual(sum_array(numbers), 7)


if __name__ == '__main__':
    unittest.main()

