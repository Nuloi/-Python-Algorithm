MOD = 1000000000
NUM = 101

N = int(input())
Arr = [[0] * 10 for _ in range(NUM)]
sum_val = [0] * NUM

for i in range(1, 10):
    Arr[1][i] = 1

for j in range(2, N + 1):
    for i in range(10):
        if i == 0:
            Arr[j][i] = Arr[j - 1][i + 1] % MOD
        elif 0 < i < 9:
            Arr[j][i] = (Arr[j - 1][i - 1] + Arr[j - 1][i + 1]) % MOD
        else:
            Arr[j][i] = Arr[j - 1][i - 1] % MOD

for i in range(10):
    sum_val[N] = (sum_val[N] + Arr[N][i]) % MOD

print(sum_val[N])
