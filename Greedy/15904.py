ucpc=input()
a=0
b=0
c=0
d=0
for i in range(len(ucpc)):
    if (a == 1 or ucpc[i] == 'U'):
        a=1
        if(b==1 or ucpc[i] =='C'):
            b=1
            if(c==1 or ucpc[i] == 'P'):
                c=1
                if( ucpc[i] == 'C'):
                    d=1
                    break
if(d==0):
    print("I hate UCPC")
else:
    print("I love UCPC")
