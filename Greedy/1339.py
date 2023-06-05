from collections import deque

N = int(input())
words = [input() for _ in range(N)]
word=words
words.sort(key=len, reverse=True)
cc=0
numdic={}

for i in range(len(words[0])):
    strlen=len(words[0])-i
    count = [0] * 26

    for j in range(N):
        if strlen == len(words[j]):
            index = ord(words[j][0]) - ord('A')
            count[index] += 1
            words[j].popleft()

    maxword=chr(ord('A') +count.index(max(count)))

    while True:
        if maxword not in numdic:
            numdic[maxword] = 9-cc
            cc+=1
        count[count.index(max(count))]=0
        if max(count)==0:
            break
        maxword=chr(ord('A') +count.index(max(count)))

print(numdic)

