# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

# Найдите количество и выведите его.

# Пример:


# list_1 = [1, 2, 3, 4, 5]
# k = 3
# # 1

# 1 способ
# list_1 = [3, 1, 2, 3, 4, 5, 3, 1]
# k = 1
# res = 0

# for i in range(len(list_1)):
#     if list_1[i] == k:
#         res = res + 1
# print(res)

# 2 способ
list_1 = [3, 1, 2, 3, 4, 5, 3, 1]
k = 3
print(list_1.count(k))
