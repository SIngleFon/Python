print("\033c")
n = int(input('Введите длину(n): '))
m = int(input('Введите ширину(m): '))
k = int(input('Введите k долек: '))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('Да')
else: print('Нет')