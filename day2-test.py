
import unittest
from day2 import Position


class TestPosition(unittest.TestCase):
    def test_axis(self):
        p = Position(0,0)
        p.move("down", 2)
        assert(p.read_displacement() == 0)   # Weird edge-case
        return

    def test_displacement(self):
        p = Position(0,0)
        p.move("down", 2)
        p.move("forward", 3)
        assert(p.read_displacement() == (2*3))
        return

if __name__ == "__main__":
    unittest.main()
