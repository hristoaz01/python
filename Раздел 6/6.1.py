from random import randint
list = []
n = 14
x = 0
for num in range(n):
    list.append(randint(1, 10))
    if (num % 2 == 0):
        x += list[num]
x *= list[n-1]
print(list)
print(x)