print("\033c")
#Ввод и Проверка  6ти значного числа
correct = bool(1)
while correct:
    try:
        number = int(input("Введите 6тизначный номер билета: "))
        if len(str(number)) == 6 and type(number) == int: 
            correct = 0
            break
    except Exception: 
        print('Ошибка ввода, введите 6 цифр: ')

# Логика
first = str(int(number) // 1000)
second = str(int(number) % 1000)
i = 0
sumFirst = 0
sumSecond = 0
while i < len(first and second):
    sumFirst = sumFirst + int(first[i])
    sumSecond += int(second[i])
    i += 1
if sumFirst == sumSecond:
    print('Билет СЧАСТЛИВЫЙ !!!')
else:
    print('Билет несчастливый. В следующий раз повезет !(')
