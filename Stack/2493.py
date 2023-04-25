n = int(input())
heights = list(map(int, input().split()))
stack = [] 

for i in range(n):
    while stack:
        if stack[-1][1] < heights[i]:
            stack.pop() 
        else:
            print(stack[-1][0], end=' ')  
            break
    if not stack:
        print(0, end=' ')
    stack.append((i+1, heights[i]))
