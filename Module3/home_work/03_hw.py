# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random
numbers = []
n = int(input("Введите количество элеменов в массиве: "))
i = 0

while i <= n-1:
    numbers.append(random.randint(-100,100))
    print(numbers[i])
    i += 1

print("-------------------")
i1 = 0
while i1 <= n-1:
    if numbers[i1] >= 0 and numbers[i1] % 2 == 0:
        print(numbers[i1])
    i1 += 1
