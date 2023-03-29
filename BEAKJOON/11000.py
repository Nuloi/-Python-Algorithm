import heapq

n = int(input())
times = []
for _ in range(n):
    s, t = map(int, input().split())
    times.append((s, t))

times.sort(key=lambda x: x[0])

count = []
for s, t in times:
    if count and count[0] <= s: 
        heapq.heappop(count)
    heapq.heappush(count, t)
print(len(count)) 
