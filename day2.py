# AoC 2021, day 2
# https://adventofcode.com/2021/day/2

import sys

class Position(object):
    def __init__(self, x, y):
        # Initial coords
        self.x = x
        self.y = y
        return

    def read_displacement(self):
        """Displacement from origin"""
        return self.x * self.y

    def move(self, dir, distance):
        assert(dir in ["up", "down", "forward", "backward"])
        if dir == "up":
            self.y -= distance
        elif dir == "down":
            self.y += distance
        elif dir == "forward":
            self.x += distance
        elif dir == "backward":
            self.x -= distance
        else:
            assert(False)
        return


if __name__ == "__main__":
    p = Position(0,0)
    for command in sys.stdin:
        (dir, dist) = command.split(maxsplit=2)
        assert(dist.isdigit())
        p.move(dir, int(dist))
    print(p.read_displacement())

