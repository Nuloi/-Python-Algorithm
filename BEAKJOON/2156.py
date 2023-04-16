n=int(input())
juices=[]
juices.append(0)
for i in range(1, n+1):
    juice = int(input())
    juices.append(juice)

if n == 1:
    print(juices[1])
elif n == 2:
    print(juices[1] + juices[2])
else:
    high = [0] * (n+1)
    high[1] = juices[1]
    high[2] = juices[1] + juices[2]

    for i in range(3, n+1):
        high[i] = max(high[i-1], high[i-2] + juices[i], high[i-3] + juices[i-1] + juices[i])
print(high[n])
        