num = int(input("Введите число: "))
if (num % 2 !=0):
    print("Плохо")
elif (num % 2 == 0) & (num >=2) &(num <=5):
    print("Неплохо")
elif (num % 2 == 0) & (num >=6) &(num <= 20):
    print("Так себе")
elif (num % 2 ==0) & (num > 20):
    print("отлично")
