N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

tetrominoes = [
    # I 테트로미노
    [
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (1, 0), (2, 0), (3, 0)]
    ],
    # L 테트로미노
    [
        [(0, 0), (1, 0), (2, 0), (2, 1)],
        [(0, 0), (0, 1), (0, 2), (1, 0)],
        [(0, 0), (0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 0), (1, 1), (1, 2)],
        [(0, 1), (1, 1), (2, 1), (2, 0)],
        [(0, 0), (1, 0), (1, 1), (1, 2)],
        [(0, 0), (0, 1), (1, 0), (2, 0)],
        [(0, 0), (0, 1), (0, 2), (1, 2)]
    ],
    # O 테트로미노
    [
        [(0, 0), (0, 1), (1, 0), (1, 1)]
    ],
    # Z 테트로미노
    [
        [(0, 0), (1, 0), (1, 1), (2, 1)],
        [(1, 0), (1, 1), (0, 1), (0, 2)],
        [(0, 1), (1, 1), (1, 0), (2, 0)],
        [(0, 0), (0, 1), (1, 1), (1, 2)],
    ],
    # T 테트로미노
    [
        [(0, 0), (0, 1), (1, 1), (0, 2)],
        [(0, 1), (1, 1), (2, 1), (1, 0)],
        [(1, 0), (1, 1), (1, 2), (0, 1)],
        [(0, 0), (1, 0), (2, 0), (1, 1)],
    ]
]


def calculate_sum(x, y, tetromino):
    total_sum = 0
    for dx, dy in tetromino:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            total_sum += paper[nx][ny]
        else:
            return 0
    return total_sum

max_sum = 0
for i in range(N):
    for j in range(M):
        for tetromino in tetrominoes:
            for shape in tetromino:
                max_sum = max(max_sum, calculate_sum(i, j, shape))

print(max_sum)
