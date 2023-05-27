import math

n = int(input())
banks = list(map(int, input().split()))
prefix = [0]
for i in range(n*2):
    prefix.append(prefix[-1]+banks[i%n])

count = 0
print(prefix)

for i in range(n-1):
    for k in range(1, n + 1):
        print(prefix[k+i], prefix[k-1])
        if prefix[k+i]<prefix[k-1]:
            count += math.ceil(abs(prefix[k+i]-prefix[k-1]) / prefix[n])
            print(count)

print(count)