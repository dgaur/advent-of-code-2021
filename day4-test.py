
import unittest
from day4 import Board, row_bingo


class TestBoard(unittest.TestCase):
    def test_nonwinner(self):
        board = [
            [ 0, 1, 2, 3, 4 ],
            [ 5, 6, 7, 8, 9 ],
            [ 9, 9, 9, 9, 9 ],
            [ 9, 9, 9, 9, 9 ],
            [ 9, 9, 9, 9, 9 ],
        ]
        b = Board(board)

        numbers = [ 5, 4, 3, 10, 11, 12 ]
        for n in numbers:
            b.play(n)
        assert(not b.winner())
        return


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


    def test_winner(self):
        board = [
            [ 0, 1, 2, 3, 4 ],
            [ 5, 6, 7, 8, 9 ],
            [ 9, 9, 9, 9, 9 ],
            [ 9, 9, 9, 9, 9 ],
            [ 9, 9, 9, 9, 9 ],
        ]
        b = Board(board)

        numbers = [ 5, 4, 3, 2, 1, 0]
        for n in numbers:
            b.play(n)

        assert(b.winner())
        return


if __name__ == "__main__":
    unittest.main()
