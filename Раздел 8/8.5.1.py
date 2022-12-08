list = [0, 9, 4, 6, 3, 9, 4, 0, 2, 3, 9]
print(list, end=' -> ')
dict = {}
for x in list:
    if x in dict.keys():
        dict[x] = 0
    else:
        dict[x] = 1
for x in list:
    if dict[x] == 1:
        list.remove(x)
print(list)
