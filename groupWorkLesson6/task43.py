nums = list(map(int, input("Введите элементы через пробел: ").split()))
count = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        if i != j:
            if nums[i] == nums[j]:
                count += 1
print(int(count / 2))

# второе решение
lst = list(map(int, input().split()))
lst1 = [lst.count(i) - 1 for i in lst]
print(lst1)
print(sum(lst1) // 2)