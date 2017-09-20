import unittest
import board


class TestBoard(unittest.TestCase):

    def test_set_get(self):
        b = board.Board()
        b.set_piece((0, 0), board.PieceType.KING)
        self.assertEqual(b[(0, 0)], board.PieceType.KING)
        self.assertEqual(b[(0, 1)], None)

    def test_err(self):
        b = board.Board()
        b.set_piece((0, 0), board.PieceType.KING)
        self.assertRaises(Exception, lambda _: b.set_piece((0, 0), board.PieceType.KING))
        self.assertRaises(Exception, lambda _: b.set_piece((0, 0), board.PieceType.BISHOP))

    def test_start(self):
        b = board.Board()
        b.reset()
        self.assertEqual(b[(0, 0)].piece_type, board.PieceType.ROOK)
        self.assertEqual(b[(7, 7)].piece_type, board.PieceType.ROOK)


if __name__ == "__main__":
    unittest.main()
