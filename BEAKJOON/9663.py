# n = int(input())
# cnt = 0
# mask =(1<<n)-1


# def n_queen(left ,col, right):
#     global cnt
    
#     if col == mask:
#         cnt+=1
#         return
    
#     fd = ~(left | col | right) & mask
    
#     while fd:
#         pos = -fd&fd
#         fd -= pos
#         n_queen((left | pos) << 1, col | pos, (right | pos) >> 1)

# n_queen(0,0,0)
# print(cnt)


n=int(input())
col=[0]*(n+1)
cnt=0

def n_queens (m):
    global cnt
    if m == n:
        cnt += 1
        return

    else:
        for i in range(n):
            col[m] = i
            if promising(m):
                n_queens(m+1)

def promising (m):
    for i in range(m):
        if col[m] == col[i] or abs(col[m] - col[i]) == abs(m - i):
            return False
    
    return True

n_queens(0)
print(cnt)