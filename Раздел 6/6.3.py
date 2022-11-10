def sort(t):
    list = []
    for i in range(len(t)):
        list.append(t[i])
    list.sort(key=abs)
    return(list)

tpl = (14, 88, -120, -7, 75, 66, 0)
print(sort(tpl))