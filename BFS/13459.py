from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(pos, dir):
    x, y = pos
    while True:
        nx, ny = x + dx[dir], y + dy[dir]
        if graph[nx][ny] == '#':
            return (x, y)
        if graph[nx][ny] == 'O':
            return None
        x, y = nx, ny

def BFS(red,blue):
    dq = deque([(red, blue)])
    cnt = 0
    
    while dq and cnt < 10:
        cnt += 1
        for _ in range(len(dq)):
            red_pos, blue_pos = dq.popleft()

            for i in range(4):
                next_red_pos = move(red_pos, i)
                next_blue_pos = move(blue_pos, i)
                
                if next_blue_pos is None:
                    continue

                if next_red_pos is None:
                    return 1
                

                if next_red_pos == next_blue_pos:
                    if i == 0:
                        if red_pos[0] > blue_pos[0]:
                            next_red_pos = (next_red_pos[0]+1, next_red_pos[1])
                        else:
                            next_blue_pos = (next_blue_pos[0]+1, next_blue_pos[1])
                    elif i == 1:
                        if red_pos[0] < blue_pos[0]:
                            next_red_pos = (next_red_pos[0]-1, next_red_pos[1])
                        else:
                            next_blue_pos = (next_blue_pos[0]-1, next_blue_pos[1])
                    elif i == 2:
                        if red_pos[1] > blue_pos[1]:
                            next_red_pos = (next_red_pos[0], next_red_pos[1]+1)
                        else:
                            next_blue_pos = (next_blue_pos[0], next_blue_pos[1]+1)
                    else:
                        if red_pos[1] < blue_pos[1]:
                            next_red_pos = (next_red_pos[0], next_red_pos[1]-1)
                        else:
                            next_blue_pos = (next_blue_pos[0], next_blue_pos[1]-1)

                dq.append((next_red_pos, next_blue_pos))

    return 0
            
    

n,m=map(int,input().split())
graph = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            red = (i, j)
        elif graph[i][j] == 'B':
            blue = (i, j)

print(BFS(red,blue))
