thickness = 5
mark = "M"
h = thickness * 5
i=0
while i < h:
    wide=thickness * 7
    j=0
    while j < wide:
        if((j >= thickness) and (j < i + thickness - thickness)) or ((j < wide - thickness) and (wide - i < j + 1)):
            print(" ", end="")
        elif j < i + thickness:
            print(mark, end="")
        elif j > wide - (thickness + i + 1):
            print(mark, end="")
        else:
            print(" ", end="")
        j += 1
    print("\r")
    i += 1