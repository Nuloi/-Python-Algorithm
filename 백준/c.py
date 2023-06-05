N = int(input())
arr = list(map(int, input().split()))

start = arr.index(min(arr))
end = start - 1
if end < 0:
    end = N - 1

count = 0 
while start != end:
    if arr[start] > arr[(start + 1) % N]: 
        count += 1
    start = (start + 1) % N

print(count + 1)
