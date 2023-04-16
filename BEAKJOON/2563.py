def area(pos):
    canvas = [[0] * 100 for _ in range(100)]

    for pos in pos:
        x, y = pos
        for i in range(10):
            for j in range(10):
                canvas[x + i][y + j] = 1

    total = sum(row.count(1) for row in canvas)
    return total

num = int(input())
pos = [tuple(map(int, input().split())) for _ in range(num)]

print(area(pos))
