# AoC 2021, day 4
# https://adventofcode.com/2021/day/4

import sys

SQUARES_PER_ROW = SQUARES_PER_COLUMN = 5

# Compute and return the specified row (bingo) of squares.  No side effects.
def row_bingo(row, square):
    bingo = dict()
    for column in range(SQUARES_PER_ROW):
        s = square[row][column]
        bingo[s] = True
    return(bingo)

# Compute and return the specified column (bingo) of squares.  No side effects.
def column_bingo(column, square):
    bingo = dict()
    for row in range(SQUARES_PER_COLUMN):
        s = square[row][column]
        bingo[s] = True
    return(bingo)

class Board(object):
    def __init__(self, square):
        # List of all possible bingos remaining
        self.bingo = []

        # Collate all possible bingos
        for row in range(SQUARES_PER_ROW):
            self.bingo.append(row_bingo(row, square))
        for column in range(SQUARES_PER_COLUMN):
            self.bingo.append(column_bingo(column, square))

        return


def read_boards(lines):
    boards = []
    rows = []
    for line in lines:
        row = [ int(number) for number in line.split() ]

        # Skip any blank lines
        if not row:
            continue

        assert(len(row) == SQUARES_PER_ROW)
        rows.append(row)
        if (len(rows) == SQUARES_PER_COLUMN):
            boards.append(Board(rows))
            rows = []

    assert(len(rows) == 0)  # no partial boards

    return(boards)


if __name__ == "__main__":
    # Read the board/square numbers
    numbers = [ int(number) for number in sys.stdin.readline().split(",") ]
    print(numbers)

    # read boards
    boards = read_boards(sys.stdin)
    assert(len(boards) > 0)


