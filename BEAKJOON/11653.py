n = int(input())
def sell(n):
    if n == 1:
        return
    cnt = 2
    while n > 1:
        if not(n % cnt):
            print(cnt)
            n //= cnt
        else:
            cnt += 1
sell(n)