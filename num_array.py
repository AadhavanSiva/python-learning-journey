import unittest
# We will define sum_array in sum_array.py later
# from sum_array import sum_array

class TestSumArray(unittest.TestCase):

    def test_empty_array(self):
        # Test case 1: Empty array
        numbers = []
        self.assertEqual(sum_array(numbers), 0)

if __name__ == '__main__':
    unittest.main()