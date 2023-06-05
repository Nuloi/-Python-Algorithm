N=int(input())
C = [int(input()) for _ in range(N)]
C.sort(reverse=1)
discount=[]
total=0
for i in range(0, len(C), 3):
    discount.append(C[i : i + 3])
for i in discount:
  if len(i) > 2:
    total += sum(i) - min(i)
  else:
    total += sum(i)
print(total)