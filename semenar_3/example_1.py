# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# 1 способ
# l = [1, 1, 2, 0, -1, 3, 4, 4]
# l = set(l)
# print(len(l))

#2 способ
list1 = [1, 1, 2, 0, -1, 3, 4, 4]
list2 = []
for i in range(len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
print(len(list2))
