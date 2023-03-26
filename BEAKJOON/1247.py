test=list()
for i in range(3):
    a=int(input())
    arr=0
    for j in range(a):
        arr+=int(input())
    if(arr==0):
        test.append('0')
    elif(arr>0):
        test.append('+')
    else:
        test.append('-')
for i in range(3):
    print(test[i])