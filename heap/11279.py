import heapq
import sys

N = int(sys.stdin.readline().strip())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline().strip())
    
    if x != 0:
        heapq.heappush(heap, (-x, x))
    else:
        if not heap:
            print(0)
        else:
            value = heapq.heappop(heap)
            print(value[1])
