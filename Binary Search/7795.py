T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B.sort()
    total = 0
    for i in A:
        low = 0
        high = len(B) - 1
        while low <= high:
            mid = (low + high) // 2
            if B[mid] < i:
                low = mid + 1
            else:
                high = mid - 1
        if high >= 0:
            total += high + 1
    print(total)
