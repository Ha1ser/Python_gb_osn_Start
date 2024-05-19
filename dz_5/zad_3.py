# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# Функция не должна ничего выводить, только возвращать значение.

# Пример:


# sum(2, 2)
# # 4

n1 = 3
n2 = 2

def sum(a, b):
    if b == 0:
        return a
    elif b < 0:
        return n1 + n2
    return sum(a + 1, b - 1) 

print(sum(n1, n2))


