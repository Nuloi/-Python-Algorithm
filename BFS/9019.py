from collections import deque

def Left(n):
    num = len(str(n))
    lt = n // (10 ** (num - 1))
    rt = (n % (10 ** (num - 1))) * 10 + lt
    return rt

def Right(n):
    num = len(str(n))
    rt = n % 10
    rlt = rt * (10 ** (num - 1)) + (n // 10)
    return rlt

def BFS(a, b):
    dq = deque([(a, "")])
    visited = set()
    visited.add(a)

    while dq:
        num, com = dq.popleft()
        if(num==b):
            return(com)
        
        new_num = num * 2
        if new_num >= 10000 and new_num not in visited:
            dq.append([new_num // 2, com + 'D'])
        else:
            dq.append([num * 2, com + 'D'])

        new_num = num - 1
        if new_num > 0 and new_num not in visited:
            dq.append([new_num, com + 'S'])
            visited.add(new_num)
        else :
            dq.append([0, com + 'S'])
            dq.append([9999, com + 'S'])
            visited.add(0)
            visited.add(9999)

        new_num = Left(num)
        if new_num not in visited:
            dq.append([new_num, com + 'L'])
            visited.add(new_num)

        new_num = Right(num)
        if new_num not in visited:
            dq.append([new_num, com + 'R'])
            visited.add(new_num)

T=int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(BFS(A,B))