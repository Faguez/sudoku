import numpy as np
r = ["A", "B", "C", "D"]
board = [
    ["A", "B", "C", "D"],
    ["", "", "", ""],
    ["", "", "", ""],
    ["", "", "A", ""]
]


def possible(y, x, n):
    coords = (y,x)
    for i in range(0, 4):
        if board[y][i] == n:
            return False
    for i in range(0, 4):
        if board[i][x] == n:
            return False
    if coords == (0, 0) or coords == (1, 1) or coords == (2,2) or coords == (3, 3):
        for i in range(0, 4):
            if np.diagonal(board)[i] == n:
                return False
    if coords == (0, 3) or coords == (1, 2) or coords == (2, 1) or coords == (3, 0):
        for i in range(0, 4):
            if np.fliplr(board).diagonal()[i] == n:
                return False
    return True


def solver():
    for y in range(1, 4):
        for x in range (0, 4):
            if board[y][x] == "":
                for n in range(4):
                    if possible(y, x, r[n]):
                        board[y][x] = r[n]
                        solver()

    print(np.matrix(board))


solver()



