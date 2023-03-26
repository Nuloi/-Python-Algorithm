def star(n):
    if n == 3:
        return ['***', '* *', '***']
    
    x = n // 3
    sub = star(x)
    result = []
    
    for i in range(n):
        if i // x == 1:
            result.append(sub[i % x] + ' ' * x + sub[i % x])
        else:
            result.append(sub[i % x] * 3)
            
    return result

n = int(input())
pattern = star(n)
for row in pattern:
    print(row)
