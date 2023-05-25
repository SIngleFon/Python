import random
n = int(input("Введи число монет: "))
count = 0
a = 0
for i in range (n):
    money = int(random.randint(0,1))
    if money == 1:
        count += 1
if int(count) > int(n-count):
    a = 1
print('Тебе нужно перевернуть = ', (count, n-count) [a], 'раз(а).')