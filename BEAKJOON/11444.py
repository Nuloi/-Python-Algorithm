n=int(input())

def fec(n):
    F = [[1, 1],[1, 0]]
    if n == 0:
        return 0
    else:
        power(n-1, F)
        return F[0][0]
    
def multi(F, b):

    x = (F[0][0] * b[0][0]) + (F[0][1] * b[1][0]) 
    y = (F[0][0] * b[0][1]) + (F[0][1] * b[1][1])
    z = (F[1][0] * b[0][0]) + (F[1][1] * b[1][0])
    w = (F[1][0] * b[0][1]) + (F[1][1] * b[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

def power(n, F):
    
    if( n == 1 or n == 0):
        return
    else:
        power(n//2, F)
        multi(F,F)
        if (n % 2) != 0:
            M = [[1, 1],[1, 0]]
            multi(F,M)
            
print(fec(n)%1000000007)
