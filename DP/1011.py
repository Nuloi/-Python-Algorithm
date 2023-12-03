T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    end = y - x
    count = 0
    move = 1
    
    while end > 0:
        count += 1
        end -= move
        
        if count % 2 == 0:
            move += 1
            
    print(count)
