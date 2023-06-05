from copy import deepcopy
def move(dir, arr):
    new_arr = deepcopy(arr)  # create a new list
    # moving process
    if dir == 0: # up
        for j in range(N):
            idx = 0
            for i in range(1, N):
                if arr[i][j]:
                    temp = arr[i][j]
                    arr[i][j] = 0
                    if arr[idx][j] == 0:
                        arr[idx][j] = temp
                    elif arr[idx][j] == temp:
                        arr[idx][j] = temp*2
                        idx += 1
                    else:
                        idx += 1
                        arr[idx][j] = temp
    elif dir == 1: # down
        for j in range(N):
            idx = N-1
            for i in range(N-2, -1, -1):
                if arr[i][j]:
                    temp = arr[i][j]
                    arr[i][j] = 0
                    if arr[idx][j] == 0:
                        arr[idx][j] = temp
                    elif arr[idx][j] == temp:
                        arr[idx][j] = temp*2
                        idx -= 1
                    else:
                        idx -= 1
                        arr[idx][j] = temp
    elif dir == 2: # left
        for i in range(N):
            idx = 0
            for j in range(1, N):
                if arr[i][j]:
                    temp = arr[i][j]
                    arr[i][j] = 0
                    if arr[i][idx] == 0:
                        arr[i][idx] = temp
                    elif arr[i][idx] == temp:
                        arr[i][idx] = temp*2
                        idx += 1
                    else:
                        idx += 1
                        arr[i][idx] = temp
    else: # right
        for i in range(N):
            idx = N-1
            for j in range(N-2, -1, -1):
                if arr[i][j]:
                    temp = arr[i][j]
                    arr[i][j] = 0
                    if arr[i][idx] == 0:
                        arr[i][idx] = temp
                    elif arr[i][idx] == temp:
                        arr[i][idx] = temp*2
                        idx -= 1
                    else:
                        idx -= 1
                        arr[i][idx] = temp
    return new_arr

def dfs(cnt, arr):
    global max_block
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                if arr[i][j] > max_block:
                    max_block = arr[i][j]
        return
    for i in range(4):
        dfs(cnt+1, move(i, deepcopy(arr)))  # safe to use the returned value

        
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dfs(0, board)
print(max_block)