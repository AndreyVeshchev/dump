num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
divisor = False
for i in range(2, min(num1, num2) + 1):
        if (num1 % i == 0) and (num2 % i == 0):
            print(i)
            divisor = True
if divisor == False:
    print("Делители отсутвуют")
