def solved(length, idx, sequence):
    if length == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(idx, N):
        sequence.append(numbers[i])
        solved(length + 1, i, sequence)
        sequence.pop()

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

solved(0, 0, [])
