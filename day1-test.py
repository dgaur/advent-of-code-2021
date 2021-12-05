
import unittest
from day1 import count_depth_increases

class TestIncreases(unittest.TestCase):
    def test_zero_increase(self):
        """Trivial base case: no depths at all"""
        assert(count_depth_increases([]) == 0)
        return


    def test_mixed_increase(self):
        depths = [  "100",
                    "200",      # increase
                    "100",
                    "200",      # increase
                    "300" ]     # increase
        assert(count_depth_increases(depths) == 3)
        return

if __name__ == "__main__":
    unittest.main()
