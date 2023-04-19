def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        half = factorial(n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * n

n = int(input())
print(factorial(n))
