# Вариант 1
number = int(input("Введите натуральное число:"))
result_sum = 0
for i in str(number):
    if int(i) % 2 == 0:
        result_sum += int(i)
print(result_sum)

# Вариант 2
number = int(input("Введите натуральное число:"))
result_sum = 0
while number > 0:
    digit = number % 10
    if digit % 2 == 0:
        result_sum += digit
    number //= 10
print(result_sum)
