# 내 풀이
def solution(board):
    k = "".join(board)
    a = k.count("O")
    b = k.count("X")
    if b > a:
        return 0
    elif abs(a - b) > 1:
        return 0
    else:
        if a > b:
            for c in range(3):
                if board[c][0] == board[c][1] == board[c][2] == "X":
                    return 0
                if board[0][c] == board[1][c] == board[2][c] == "X":
                    return 0
            if board[0][0] == board[1][1] == board[2][2] == "X":
                return 0
            elif board[0][2] == board[1][1] == board[2][0] == "X":
                return 0
            return 1
        else:
            for c in range(3):
                if board[c][0] == board[c][1] == board[c][2] == "O":
                    return 0
                if board[0][c] == board[1][c] == board[2][c] == "O":
                    return 0
            if board[0][0] == board[1][1] == board[2][2] == "O":
                return 0
            elif board[0][2] == board[1][1] == board[2][0] == "O":
                return 0
            return 1

# 다른 사람 풀이
# Check if there is a winning row, column, or diagonal
def check_win(player, board):
    # Check rows
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True

    # Check columns
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def solution(board):
    num_x = sum(row.count('X') for row in board)
    num_o = sum(row.count('O') for row in board)

    if num_x - num_o > 0 or abs(num_x - num_o) > 1:
        return 0

    elif (check_win('O', board) and num_x != num_o - 1) or (check_win('X', board) and num_x != num_o):
        return 0

    return 1