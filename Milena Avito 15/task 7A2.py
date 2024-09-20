num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
for i in range(2, min(num1, num2) + 1):
        if (num1 % i == 0) and (num2 % i == 0):
            print(i)
