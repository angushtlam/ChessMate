from board import Board


class State:
    """
    The logical states of the game
    """
    GAME_STARTING = 0
    WAITING_FOR_INPUT = 1
    SHOWING_MOVES = 2


# Game data
chess_board = Board()
active_piece = None
active_location = None
state = State.GAME_STARTING


def toggle_piece(coord):
    """
    Event: A piece was lifted or set down at the specified coordinate
    :param coord: A 2-tuple representing the (row, col) coordinate on the board
    :return: An array - The first index is the command, the second is the parameters (Ex: [on, [(1, 1), (2, 3)])
    """
    global chess_board
    global active_piece
    global active_location
    global state

    row, col = coord[0], coord[1]
    assert 0 <= row <= 7 and 0 <= col <= 7

    # If there was already a piece here, this must be a lift event
    if chess_board[coord] is not None:
        state = State.SHOWING_MOVES

        if active_piece is None:
            active_piece = chess_board.remove_piece(coord)
            active_location = coord
            return ['on', active_piece.get_moves(active_location, chess_board)]
        else:
            raise Exception("Second piece picked up")
    else:
        # Otherwise, this must be a set down event
        # Ensure that there is an active piece
        state = State.WAITING_FOR_INPUT

        if active_piece is not None:
            # Set down the active piece at the given location
            chess_board.set_piece(coord, active_piece)

            positions = active_piece.get_moves(active_location, chess_board)

            active_piece = None
            active_location = None

            return ['off', positions]
        else:
            raise Exception("Attempted to set down a piece before piece was selected")


def start():
    """
    Initialize a new game
    :return: None
    """
    global chess_board
    global state

    chess_board.reset()
    state = State.WAITING_FOR_INPUT