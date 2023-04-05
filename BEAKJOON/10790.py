def min_check_count(l, v1, v2, t, s):
    time_min = l / v1
    time_max = l / v2
    min_distance = v1 * s
    max_distance = v2 * s

c = int(input())

for _ in range(c):
    l, v1, v2, t, s = map(int, input().split())
    result = min_check_count(l, v1, v2, t, s)
    print(result)
