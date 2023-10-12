import heapq
import sys

N = int(sys.stdin.readline().strip())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline().strip())
    
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if not heap:
            print(0)
        else:
            min_value = heapq.heappop(heap)
            print(min_value[1])
