value = int(input("Введите ваше число: "))
if (value % 3 == 0) and (value % 5 == 0):
    print("Fizz Buzz")
elif value % 3 == 0:
    print("Fizz")
elif value % 5 == 0:
    print("Buzz")
else:
    print(value)
