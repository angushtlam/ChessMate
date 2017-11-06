from board import PieceType
from util import detect_check

# Inputs: Board, King being moved, Coords as a tuple (x, y)
def can_castle(board, king, coords):
    # Piece must be King.
    if king.piece_type != PieceType.KING:
        return False

    # The king and the chosen rook are on the player's first rank.
    layer = 0 if piece_type.is_black else 7

    # Try and find the rook
    rook = board[layer][coords[1]]
    if rook != PieceType.ROOK:
        return False
    
    # Check that they're the same color.
    if king.is_black != rook.is_black:
        return False

    # Neither the king nor the chosen rook has previously moved
    if king.moved or rook.moved:
        return False

    # There are no pieces between the king and the chosen rook
    for x in range(min(coords[0], 4) + 1, max(coords[0], 4) - 1):
        if board[layer][x] is not None:
            return False

    # The king is not currently in check.
    if detect_check(piece):
        return False

    return True