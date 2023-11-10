N, M = map(int, input().split())

stack = []

start = 1

while True:
    if len(stack) == M:
        print(' '.join(map(str, stack)))
        start = stack.pop() + 1 
    if start > N: 
        if not stack:
            break
        start = stack.pop() + 1 
    else:
        stack.append(start)
        start += 1
