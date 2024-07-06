import sys
import unittest
import random
from sum import sum_array

class TestSumFunction(unittest.TestCase):
    def test_sum_empty_array(self):
        expected_sum = 0

        array = []
        length= len(array)
        
        result = sum_array(array, length)
        self.assertEqual(result, expected_sum)

    def test_sum_single_element_array(self):
        expected_sum = 42

        array = [42]
        length= len(array)

        result = sum_array(array, length)
        self.assertEqual(result, expected_sum)

    def test_sum_array_with_zeros(self):
        expected_sum = 0

        array = [0, 0, 0, 0, 0]
        length= len(array)

        result = sum_array(array, length)
        self.assertEqual(result, expected_sum)

if __name__ == '__main__':
    unittest.main()