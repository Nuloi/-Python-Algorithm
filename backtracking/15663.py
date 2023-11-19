def solved(length, idx, q):
    if length == M:
        print(' '.join(map(str, q)))
        return
    
    for i in range(idx, N):
        q.append(numbers[i])
        solved(length + 1, i, q)
        q.pop()

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

solved(0, 0, [])
