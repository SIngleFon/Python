print("\033c")
sum = int(input('Кол-во журавликов: '))
if sum % 6 == 0: 
    sum /= 6
    print('Петя сделал =', int(sum), 'Сережа сделал =', int(sum), 'Катя сделала =', int(sum * 4))
else:
    print('Невозможно посчитать')