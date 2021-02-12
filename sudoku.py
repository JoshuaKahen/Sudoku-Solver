# Finds empty spots in the puzzle and then gives back their location
def empty(board):
    for i in range(0, 9):
        for j in range(0, 9):
            # The function will send back the location is the number is equal to zero
            if board[i][j] == 0:
                return i, j

    return None


# Checks if certain spot on the board is valid for a number
def valid(board, number, pos):
    # Checks if number is repeated in the row
    for i in range(0, 9):
        # If the number is the same as the original number and the position is not the same it will return false
        if board[pos[0]][i] == number and pos[1] != i:
            return False

    # Checks if number is repeated in the column
    for i in range(0, 9):
        # If the number is the same as the original number and the position is not the same it will return false
        if board[i][pos[1]] == number and pos[0] != i:
            return False

    # Checks if number is repeated in the box
    for i in range((pos[0] // 3) * 3, (pos[0] // 3) * 3 + 3):
        for j in range((pos[1] // 3) * 3, (pos[1] // 3) * 3 + 3):
            # If the number is the same as the original number and the position is not the same it will return false
            if board[i][j] == number and (i, j) != pos:
                return False

    return True


# Solves board by using the backtracking method
def solve(board):
    find = empty(board)
    if not find:
        return True
    else:
        row, col = find

    # Goes through each box in the puzzle
    # With one of the possible numbers in the chain
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False
