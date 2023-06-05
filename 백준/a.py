import math

N, R = map(int, input().split())
X = N - R
total = 0

for i in range(1, int(math.sqrt(X)) + 1):
    if X % i == 0:
        if i > R:
            total += i
        if X // i != i and X // i > R:
            total += X // i
            
print(total)
