sc=input()
ko=0
yo=0
knum=0
ynum=0
if "K" in sc:
        if "O" in sc[sc.index("K"):]:
            if "R" in sc[sc.index("O"):]:
                if "E" in sc[sc.index("R"):]:
                    if "A" in sc[sc.index("E"):]:
                        ko=1
                        print(sc[sc.index("E"):sc.index("A")])
if "Y" in sc:
    if "O" in sc[sc.index("Y"):]:
        if "N" in sc[sc.index("O"):]:
            if "S" in sc[sc.index("N"):]:
                if "E" in sc[sc.index("S"):]:
                    if "I" in sc[sc.index("E"):]:
                        yo=1
                        ynum=sc.index("I")

if ko==1 and yo==1:
    if ynum>knum:
        print("KOREA")
    else:
        print("YONSEI")
elif ko==1:
        print("KOREA")
elif yo==1:
        print("YONSEI")