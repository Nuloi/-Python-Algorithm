formula = input()
stack=[]
Postfix=''

mode=["+","-", "*", "/", "(",")"]

for i in formula:
    if i not in mode:
        Postfix += i
    elif i== ')':
            while stack and stack[-1]!='(':
                Postfix += stack.pop()
            stack.pop()
    else:
        if i=='(':
            stack.append(i)         
        elif i== ')':
            while stack and stack[-1]!='(':
                Postfix += stack.pop()
            stack.pop()
        elif i=='*' or i=='/': 
            while stack and (stack[-1]=='*'or stack[-1]=='/'):
                Postfix += stack.pop()
            stack.append(i)
        elif i=='+' or i=='-':
            while stack and stack[-1]!='(':
                Postfix += stack.pop() 
            stack.append(i)
while stack:
    Postfix+=stack.pop()

print(Postfix)
