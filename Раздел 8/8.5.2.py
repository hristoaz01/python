x = 0
y = 0
z = 1
n = 2

number_of_permutations = 0
permutations_list = []
if x != y != z:
    number_of_permutations = 27
elif x == y == z:
    number_of_permutations = 1
else:
    number_of_permutations = 8

for i in range(number_of_permutations):
    num = i
    new_num = ''
    permutation = [0, 0, 0]
    if num == 0:
        new_num = 0
    else:
        while num > 0:
            new_num = str(int(num % (number_of_permutations ** (1. / 3.)))) + new_num
            num //= (number_of_permutations ** (1 / 3))
    j = 3
    while j:
        permutation[j - 3] = int(new_num) - (int(new_num) // 10) * 10
        new_num = int(new_num) // 10
        j -= 1
    if number_of_permutations == 27:  ### !ОСТОРОЖНО! - БЫДЛОКОД ###
        for h in range(len(permutation)):
            match permutation[h]:
                case 0:
                    permutation[h] = x
                case 1:
                    permutation[h] = y
                case 2:
                    permutation[h] = z
    if number_of_permutations == 8:
        for h in range(len(permutation)):
            match permutation[h]:
                case 0:
                    if x == y: permutation[h] = x
                    if x == z: permutation[h] = z
                    if y == z: permutation[h] = y
                case 1:
                    if x == y: permutation[h] = z
                    if x == z: permutation[h] = y
                    if y == z: permutation[h] = x
    if number_of_permutations == 1:
        permutation = [x, y, z]
    permutations_list.append(permutation)
print(f'x = {x}, y = {y}, z = {z}, n = {n}\nрезультат: {permutations_list}')
