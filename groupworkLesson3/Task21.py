# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

# dictionary = {}
dictionary  = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": " S005 "}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}]
# list = set()
# for i in dictionary: 
#     for j in i.keys():
#         list.add(i[j].strip())
# print(list)

print(set([list(i.values())[0].strip() for i in dictionary]))