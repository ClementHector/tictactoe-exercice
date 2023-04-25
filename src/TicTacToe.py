

def get_winner(tuple: list) -> bool:
    if tuple[0] == tuple[1] == tuple[2] and tuple[0] != 0:
        return tuple[0]

def is_unfinished(tuple_board: list) -> bool:
    return True if tuple_board.count(0) > 0 else False

def get_rows(board: list) -> list:
    return [tuple(row) for row in board]

def get_columns(board: list) -> list:
    return list(zip(*board))

def get_diagonals(board: list) -> list:
    diag1 = [board[i][i] for i in range(3)]
    diag2 = [board[i][2-i] for i in range(3)]
    return [diag1, diag2]

def check_board(board: list) -> int:
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
