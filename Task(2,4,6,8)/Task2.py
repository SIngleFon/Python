print("\033c")
# "Сложный метод"
number = int(input('Введите трехзначное число для "сложного" метода: '))
print('Сложный метод =', number % 10+((number // 10) %10)+((number // 10)//10))

# Легкий метод
numberr = input('Введите трехзначное число для легкого метода: ')
i = 0
sum = 0
while i < len(numberr):
    sum += int(numberr[i])
    i += 1
print('Легкий метод', '=', sum )