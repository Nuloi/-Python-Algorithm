import heapq
import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    q = []
    k = int(sys.stdin.readline().strip())
    
    for _ in range(k):
        x, num = sys.stdin.readline().split()
        num = int(num)
        
        if x == 'I':
            heapq.heappush(q, num)
        if x == 'D':
            if num == 1:
                if len(q) != 0:
                    value = max(q)
                    q.remove(value)
            else:
                if len(q) != 0:
                    heapq.heappop(q)
    
    if len(q) == 0:
        print("EMPTY")
    else:
        print(max(q), heapq.heappop(q))