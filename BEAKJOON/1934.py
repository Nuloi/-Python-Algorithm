def gcd(m,n):
    if n == 0:
        return m
    mod = m % n
    if mod != 0:
        m, n = n, mod
        return gcd(m, n)
    else:
        return n
a=input()
for i in range(a):
    n,m=map(int,input().split())
    print(round((n*m)/gcd(m,n)))
