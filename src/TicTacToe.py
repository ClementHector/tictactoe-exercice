
def get_winner(three_cells: tuple) -> bool:
    """Returns the winner if there is one, else returns None
    param three_cells: a tuple representing a row, column, or diagonal (3 cells)
    like (0,0,0)
    return: 1 if player X wins, 2 if player O wins, else None
    """
    if three_cells[0] == three_cells[1] == three_cells[2] and three_cells[0] != 0:
        return three_cells[0]

def is_unfinished(three_cells: tuple) -> bool:
    """Returns True if there are any empty cells, else returns False
    param three_cells: a tuple representing a row, column, or diagonal (3 cells)
    like (0,0,0)
    return: True if there are any empty cells, else False
    """
    return three_cells.count(0) > 0

def get_rows(board: list) -> list:
    """Returns a list of tuples representing the rows of the board
    param board: a list of lists representing the board
    return: a list of tuples representing the rows of the board
    """
    return [tuple(row) for row in board]

def get_columns(board: list) -> list:
    """Returns a list of tuples representing the columns of the board
    param board: a list of lists representing the board
    return: a list of tuples representing the columns of the board
    """
    return list(zip(*board))

def get_diagonals(board: list) -> list:
    """Returns a list of tuples representing the diagonals of the board
    param board: a list of lists representing the board
    return: a list of tuples representing the diagonals of the board
    """
    diag1 = [board[i][i] for i in range(3)]
    diag2 = [board[i][2-i] for i in range(3)]
    return [diag1, diag2]

def check_board(board: list) -> int:
    """Returns 1 if player 1 wins, 2 if player 2 wins, 0 if it's a tie,
    and -1 if the game is unfinished
    param board: a list of lists representing the board
    return: 1 if player 1 wins, 2 if player 2 wins, -1 if the game is
    unfinished, else 0 if it's a cat's game
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