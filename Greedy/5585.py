b=int(input())
a=1000-b
totalcoin=0
while a!=0:
    if a>=500:
        a-=500
        totalcoin+=1
    elif a>=100:
        a-=100
        totalcoin+=1
    elif a>=50:
        a-=50
        totalcoin+=1
    elif a>=10:
        a-=10
        totalcoin+=1
    elif a>=5:
        a-=5
        totalcoin+=1
    elif a>=1:
        a-=1
        totalcoin+=1
print(totalcoin)
