while True:
    string = input().rstrip() 
    if string == ".":  
        break

    stack = []  
    balanced = True 
    for char in string:
        if char in "([":
            stack.append(char)
        elif char in ")]":
            if not stack or (char == ")" and stack[-1] != "(") or (char == "]" and stack[-1] != "["):
                balanced = False
                break
            stack.pop()

    if balanced and not stack:
        print("yes")
    else:
        print("no")
