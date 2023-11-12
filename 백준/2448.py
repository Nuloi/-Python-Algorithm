def star(x, y, length, matrix):
    if length == 3:
        matrix[y][x + 2] = '*'
        matrix[y + 1][x + 1] = '*'
        matrix[y + 1][x + 3] = '*'
        for i in range(x, x + 5):
            matrix[y + 2][i] = '*'
        return

    small = length // 2

    star(x + small, y, small, matrix)
    star(x, y + small, small, matrix)
    star(x + length, y + small, small, matrix)


n = int(input())
matrix = [[' ']*(2*n - 1) for _ in range(n)]

star(0, 0, n, matrix)

for y in range(n):
    print(''.join(matrix[y]))
