def is_valid_sudoku(board):
    for row in board:
        digits = set(row)
        if len(digits) != 9:
            return False

    for col in board:
        digits = set([board[row][col] for row in range(9)])
        if len(digits) != 9:
            return False

    for row_start in range(0, 9, 3):
        for col_start in range(0, 9, 3):
            sub_box = [board[row][col] for row in range(row_start, row_start + 3) for col in range(col_start , col_start + 3)]
            digits = set(sub_box)
            if len(digits) != 9:
                return False


    return True

