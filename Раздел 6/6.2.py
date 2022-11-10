from random import randint
list = []
num = 0
n = 10
for num in range(n):
    list.append(randint(-20, 20))
print(list)
list.sort()
print(list)
print(list[9], ' - ', list[0], ' = ', (list[9] - list[0]))