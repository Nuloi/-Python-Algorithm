N = int(input())
K = int(input())

left = 1
right = K
ans = 0

while left <= right :
    cnt = 0
    mid = (left+right) // 2

    for i in range(1, N+1):
        cnt += min(mid // i, N)

    if cnt < K :
        left = mid + 1
    else :
        ans = mid
        right = mid - 1

print(ans)
