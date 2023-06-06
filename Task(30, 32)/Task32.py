# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

rang, diap, userList, inpt = list(map(int, input("Введите через пробел мин и макс диапазон: ").split())), list(),list(), list()
userKey = int(input("Желаете сами ввести массив? 1 - да, 0 - нет: "))
if userKey == 1:
    userList = list(map(int, input("Введите через пробел элементы массива: ").split()))
else:
    userList = [-5, 9, 0, 3, -1, -2, 1,
                4, -2, 10, 2, 0, -9, 8, 
                10, -9, 0, -5, -5, 7]

for i in range((rang[1] - rang[0]) + 1):
    diap.append(rang[0] + i)
print(diap)

for i in range(len(userList)):
    for j in range(len(diap)):
        if userList[i] == diap[j]:
            inpt.append(i)
print(inpt)