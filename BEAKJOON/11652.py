n = int(input())

cards = {}
for i in range(n):
    num = int(input())
    if num in cards:
        cards[num] += 1
    else:
        cards[num] = 1

max_count = 0
max_num = 0
for num, count in cards.items():
    if count > max_count:
        max_count = count
        max_num = num
    elif count == max_count and num < max_num:
        max_num = num

print(max_num)
