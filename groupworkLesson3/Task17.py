import random
print("\033c")
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
number = int(input("Введите максимум чисел: "))
num = []
for i in range (number):
    num.append(random.randint(-3, 3))
print (num)
print(len(set(num)))


print(len(set(input().split())))