
import unittest
from day1 import count_depth_increases

class TestIncreases(unittest.TestCase):
    def test_zero_increase(self):
        assert(count_depth_increases([]) == 0)
        return


if __name__ == "__main__":
    unittest.main()
