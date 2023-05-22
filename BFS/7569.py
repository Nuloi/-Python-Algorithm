from collections import deque

def BFS (m, n, h, box):
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    days = 0

    rt= deque()
    urt = 0

    for z in range(h):
        for y in range(n):
            for x in range(m):
                if box[z*n + y][x] == 1:
                    rt.append((x, y, z))
                elif box[z*n + y][x] == 0:
                    urt += 1

    while rt:
        ct = len(rt)
        while ct > 0:
            x, y, z = rt.popleft()
            ct -= 1
            for i in range(6):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    nz = z + dz[i]

                    if nx < 0 or nx >= m or ny < 0 or ny >= n or nz < 0 or nz >= h:
                        continue

                    if box[nz*n + ny][nx] == 0:
                        box[nz*n + ny][nx] = 1
                        rt.append((nx, ny, nz))
                        urt -= 1
        days += 1
    
    if urt == 0:
        return days - 1
    else:
        return -1


m, n, h= map(int, input().split())
box = []
for i in range(n * h):
    box.append(list(map(int, input().split())))

print(BFS(m, n, h, box))
