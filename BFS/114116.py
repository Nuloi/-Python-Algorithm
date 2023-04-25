from collections import deque

s = int(input())

init_state = (1, 0, 0)

dq = deque([init_state])
visited = set([init_state])

while dq:
    screen, clips, time = dq.popleft()

    if screen == s:
        print(time)
        break

    new_state = (screen, screen, time+1)
    if new_state not in visited:
        dq.append(new_state)
        visited.add(new_state)

    if screen+clips <= s:
        new_state = (screen+clips, clips, time+1)
        if new_state not in visited:
            dq.append(new_state)
            visited.add(new_state)

    if screen > 1:
        new_state = (screen-1, clips, time+1)
        if new_state not in visited:
            dq.append(new_state)
            visited.add(new_state)
