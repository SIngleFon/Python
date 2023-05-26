# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
print("\033c")

list = [1, 2, 3, 4, 5]
k = int(input("Введи k: "))
print(list)
list = list[k:] + list[:k]
print(list)

list = [1, 2, 3, 4, 5]
for i in range(k-1):
    tmp = list[-1]
    list.insert(0, tmp)
    list.pop()
print(list)

list = [1, 2, 3, 4, 5]
for i in range(k):
    t=list[0]
    for i in range(len(list)-1):
        list[i]=list[i+1]
    list[-1]=t
print(list)


list = [1, 2, 3, 4, 5]
for i in range(k-1):
    list.insert(0, list.pop()) # pop - последний. insert на нулевое 
print(list)  