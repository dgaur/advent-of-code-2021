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

    def play(self, number):
        """Play a new number on this bingo board"""
        for bingo in self.bingo:
            # Remove the square if present
            bingo.pop(number, None)
        return

    def remainder(self):
        """Sum up the remaining, undrawn squares.  No side effects"""
        remainder = sum(square for bingo in self.bingo for square in bingo.keys())

        # Cut in half, since each remaining square is double-counted, once in each direction
        return int(remainder/2)


    def winner(self):
        """Did this board win?"""
        # A blank bingo means all squares in that row/column have been drawn (i.e., no
        # squares are left in that row/column)
        return [ bingo for bingo in self.bingo if len(bingo) == 0 ]


def read_boards(lines):
    """
    Compute + return a list of boards from text input. No side effects.
    """
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

    # Read the individual bingo boards
    boards = read_boards(sys.stdin)
    assert(len(boards) > 0)

    # Now play bingo.  Apply each new number/square in turn until some board wins or
    # all numbers are exhausted
    for number in numbers:
        for board in boards:
            board.play(number)

            # Did this board just win?
            if board.winner():
                remainder = board.remainder()
                score = number * remainder
                print(f"Winner! Reminder {remainder}, final score {score}")
                sys.exit()


    # else, no winner
    print("No winner")




