# Advent of code 2021, day 1
# https://adventofcode.com/2021/day/1

import sys


def count_depth_increases(text):
    """
    Count the number of times the depth increases from previous depth.
    No side effects
    """
    last_depth = 65535
    increases = 0

    for line in text:
        depth = int(line)
        if (depth > last_depth):
            increases += 1
        last_depth = depth
    return increases

if __name__ == "__main__":
    print(count_depth_increases(sys.stdin))



