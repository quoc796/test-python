import numpy as np

grid =  [[8, 7, 6, 9, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 6, 0, 0, 0],
         [0, 4, 0, 3, 0, 5, 8, 0, 0],
         [4, 0, 0, 0, 0, 0, 2, 1, 0],
         [0, 9, 0, 5, 0, 0, 0, 0, 0],
         [0, 5, 0, 0, 4, 0, 3, 0, 6],
         [0, 2, 9, 0, 0, 0, 0, 0, 8],
         [0, 0, 4, 6, 9, 0, 1, 7, 3],
         [0, 0, 0, 0, 0, 1, 0, 0, 4]]


def possible(x, y, n):
    global grid
    for i in range(9):
        if grid[x][i] == n:
            return False

    for i in range(9):
        if grid[i][y] == n:
            return False
    x_start = (x // 3) * 3
    y_start = (y // 3) * 3

    for i in range(3):
        for j in range(3):
            if grid[x_start + i][y_start + j] == n:
                return False

    return True


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(np.matrix(grid))
    input("More ?")

print(np.matrix(grid))
solve()
