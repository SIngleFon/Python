# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n
#  = a1
#  + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

user = list(map(int, input("Введите через пробел (1e) (Разность) (Кол-во элементов): ").split()))
list = list()
list.append(user[0])
for i in range(user[2] - 1):
    list.append(list[i] + user[1])
print(list)