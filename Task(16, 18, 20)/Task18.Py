import random
N = int(input("Введи кол-во элементов в коллекции: "))
X = int(input("Введи элемент: "))
bol = 1 # Выставляем булевое значение на тру)

# Заполнение коллекции
list = []
for i in range (N):
    list.append(random.randint(-25, 25)) # Заполняет коллекцию цифрами от -25 до 25. 
print(list)


# Логика: 
for i in range (len(list)):
    if list[i] == X:
        print(f"Число {list[i]} есть в коллекции, и находится по индексу {i}")
        bol = 0
        break

if (bol == 1):
    temp = abs(X - list[0])
    j = 0
    for i in range (len(list)):
        t = abs(X - list[i])
        if t < temp:
            temp = t
            j = i
    print(f'Число {list[j]}, максимально близко к искомому {X}')