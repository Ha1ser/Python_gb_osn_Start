# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

# Пример:


# list_1 = [1, 2, 3, 4, 5]
# k = 6
# # 5

# 1 способ
# list_1 = [1, 2, 3, 4, 5]
# k = 6


# closest_num = None      # none значит пусто
# min_diff = float('inf')   # float('inf') обозначает бесконечность

# for num in list_1:
#     diff = abs(num - k)
#     if diff < min_diff:
#         min_diff = diff
#         closest_num = num

# print(closest_num)



# 2 способ
list_1 = [1, 4, 5, 8, 12, 13, 17]
k = 10

list_1.append(k)
list_1 = sorted(list_1)
for i in range(len(list_1)):
    if k == list_1[len(list_1) - 1]:
        print(list_1[len(list_1) - 2])
        break
    elif k == list_1[0]:
        print(list_1[1])
        break
    elif k == list_1[i]:
        min1 = list_1[i - 1]
        max1 = list_1[i + 1] 
        if abs(k - min1) < abs(k - max1):
            print(min1)
            break
        else:
            abs(k - min1) > abs(k - max1)
            print(max1)
            break
    else:
        i = i + 1