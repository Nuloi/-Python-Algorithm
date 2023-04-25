def AC(p, n, arr):
    lst = arr.strip('[]\n').split(',')
    if lst == ['']: lst = []
    
    rev = False 
    for func in p:
        if func == 'R':
            rev = not rev
        elif func == 'D':
            if not lst:
                print('error')
                return
            if rev:
                lst.pop()
            else:
                lst.pop(0)
    
    if rev:
        lst.reverse()
    
    print('[', end='')
    for i in range(len(lst)):
        if i == len(lst) - 1:
            print(lst[i], end='')
        else:
            print(lst[i], end=',')
    print(']')

T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    arr = input()
    AC(p, n, arr)
