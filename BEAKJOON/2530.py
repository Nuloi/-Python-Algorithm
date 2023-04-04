h, m, s = map(int, input().split())
ns = int(input())

hour = h + ((m + ((s + ns) // 60)) // 60)
min = (m + ((s + ns) // 60)) % 60
sec = (s + ns) % 60

while hour >= 24 :
  hour = hour - 24

print(hour,min,sec)