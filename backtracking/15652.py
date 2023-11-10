N, M = map(int, input().split())

stak = [0] * M

def solved(index, start):
    if index == M:
        print(*stak)
        return

    for i in range(start, N + 1):
        stak[index] = i
        solved(index + 1, i)

solved(0, 1)