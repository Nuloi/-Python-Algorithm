def min_magic_moves(n, capitals):
    magic_moves = 0

    while any(k < 0 for k in capitals):
        min_abs_negative = float('inf')
        min_index = -1
        for i, k in enumerate(capitals):
            if k < 0 and abs(k) < min_abs_negative:
                min_abs_negative = abs(k)
                min_index = i

        magic_moves += min_abs_negative
        capitals[min_index] = abs(capitals[min_index])
        capitals[(min_index - 1) % n] -= min_abs_negative
        capitals[(min_index + 1) % n] -= min_abs_negative

    return magic_moves

n = int(input())
capitals = list(map(int, input().split()))

result = min_magic_moves(n, capitals)
print(result)
