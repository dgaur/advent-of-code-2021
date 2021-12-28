
import unittest
from day4 import Board, row_bingo


class TestBoard(unittest.TestCase):
    def test_row_bingo(self):
        board = [
            [ 0, 1, 2, 3, 4 ],
            [ 5, 6, 7, 8, 9 ],
            # other rows unused
        ]

        bingo = row_bingo(0, board)
        for square in board[0]:
            assert(square in bingo)
        return


if __name__ == "__main__":
    unittest.main()
