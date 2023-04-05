def calc_bt(N, M, t_h, l_h):
    r_b, rm_b = 0, 0

    for i in range(N):
        for j in range(M):
            d = l_h[i][j] - t_h
            if d > 0:
                rm_b += d
            else:
                r_b -= d

    t = rm_b * 2 + r_b
    return r_b, rm_b, t


def min_tf_land(N, M, B, l_h):
    min_t, max_h = float('inf'), 0

    for t_h in range(257):
        r_b, rm_b, t = calc_bt(N, M, t_h, l_h)

        if r_b <= rm_b + B:
            if t < min_t:
                min_t, max_h = t, t_h
            elif t == min_t and t_h > max_h:
                max_h = t_h

    return min_t, max_h


N, M, B = map(int, input().split())
l_h = [list(map(int, input().split())) for _ in range(N)]

min_t, max_h = min_tf_land(N, M, B, l_h)
print(min_t, max_h)
