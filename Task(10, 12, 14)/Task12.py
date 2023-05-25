n1 = int(input("Введи первое число: "))
n2 = int(input("Введи второе число: "))
for i in range (n1):
    for k in range (n2):
        if(n1 == i + k) and (n2 == i * k):
            print(f"x1 = {i}, x2 = {k}")