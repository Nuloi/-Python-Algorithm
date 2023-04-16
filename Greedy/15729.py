N = int(input())
target = list(map(int, input().split()))

buttons = [0] * N
count = 0

for i in range(N):
    if buttons[i] != target[i]:
        count += 1
        buttons[i] ^= 1
        if(i<N-2):
            buttons[i + 2] ^= 1
        if(i<N-1):
            buttons[i + 1] ^= 1

if buttons[-2:] != target[-2:]:
    count += 1
print(count)