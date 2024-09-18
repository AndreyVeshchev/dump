N = int(input("Введите размер списка чисел: "))
numbers = [int(x) for x in input("Введите числа через пробел: ").split()][:N]
K = int(input("Введите K: "))
L = int(input("Введите L: "))
total_sum = 0
for i in range(len(numbers)):
    if not (K - 1 <= i <= L - 1):
        total_sum += numbers[i]
print(total_sum)
