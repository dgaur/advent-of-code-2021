# Advent of code 2021, day 1
# https://adventofcode.com/2021/day/1

import sys


def count_depth_increases(text):
    last_depth = 65535
    increases = 0

    for line in text:
        depth = int(line)
        if (depth > last_depth):
            increases += 1
        last_depth = depth
    return increases

print(count_depth_increases(sys.stdin))



