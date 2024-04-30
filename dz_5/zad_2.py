# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.

# Функция не должна ничего выводить, только возвращать значение.

# Пример:


# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8 

# 1 способ
# def step(a, b):
#     if b == 0:
#         return 1
#     elif b < 0:
#         return 1 / step(a, -b)
#     elif b % 2 == 0:
#         return step(a, b // 2) ** 2
#     else:
#         print(a, b, "*")
#         return a * step(a, b - 1) 

# print(step(2, 4)) 


# 2 способ
def f(a, b):
    if b == 0:
        return 1
    elif b > 0:
        print(a, b)
        return a * f(a, b - 1)
    else:
        return 1 / (a * f(a, -b - 1)) 


print(f(5, 3))






