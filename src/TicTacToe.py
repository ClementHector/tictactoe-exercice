

def get_winner(tuple: list) -> bool:
    """Returns the winner if there is one, else returns None
    """
    if tuple[0] == tuple[1] == tuple[2] and tuple[0] != 0:
        return tuple[0]

def is_unfinished(tuple_board: list) -> bool:
    """Returns True if there are any empty cells, else returns False"""
    return tuple_board.count(0) > 0

def get_rows(board: list) -> list:
    """Returns a list of tuples representing the rows of the board"""
    return [tuple(row) for row in board]

def get_columns(board: list) -> list:
    """Returns a list of tuples representing the columns of the board"""
    return list(zip(*board))

def get_diagonals(board: list) -> list:
    """Returns a list of tuples representing the diagonals of the board"""
    diag1 = [board[i][i] for i in range(3)]
    diag2 = [board[i][2-i] for i in range(3)]
    return [diag1, diag2]

def check_board(board: list) -> int:
    """Returns 1 if player 1 wins, 2 if player 2 wins, 0 if it's a tie,
    and -1 if the game is unfinished
    """
    rows = get_rows(board)
    cols = get_columns(board)
    diags = get_diagonals(board)

    for tuple in rows + cols + diags:
        winner = get_winner(tuple)
        if winner:
            return winner

    if is_unfinished([cell for row in board for cell in row]):
        return -1

    return 0
