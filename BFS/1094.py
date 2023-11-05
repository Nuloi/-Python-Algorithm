X = int(input())
count = 0

while X > 0:
    if X >= 64:
        X -= 64
        count += 1
    else:
        for i in [32, 16, 8, 4, 2, 1]:
            if X >= i:
                X -= i
                count += 1
                break

print(count)
