import random
N = int(input("Введи кол-во элементов в коллекции: "))
X = int(input("Введи искомый элемент: "))
list = []
count = 0

# Заполнение коллекции
for i in range (N):
    list.append(random.randint(1, 3)) # Заполняет коллекцию цифрами от 1 до 3. 
print(list)



# 1 Решение
for i in range (N):   
    if(list[i] == X): count += 1  # в данный цикл можно просто вставить list.append(random.randint(1, 3)) и выполнить всё 1ым решением.
print(count)


# 2 Решение
print(sum(list[i] == X for i in range(N)))
print(sum)