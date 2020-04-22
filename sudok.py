import numpy as np
r = ["A", "B", "C", "D"]
board = [
    ["A", "B", "C", "D"],
    ["", "", "", ""],
    ["", "", "B", ""],
    ["", "", "", ""]
]

def possible(y,x,n):
    for i in range(0, 4):
        if board[y][i] == n:
            return False
    for i in range(0, 4):
        if board[i][x] == n:
            return False
    return True

print(possible(1,0,"A"))


print(np.matrix(board))

