# Найдите сумму цифр трехзначного числа n.

# Результат сохраните в перменную res.

# Пример:


# n = 123 -> res = 6 (1 + 2 + 3)

# n = 100 -> res = 1 (1 + 0 + 0)

n = int(input())

n1 = n // 100
n2 = n // 10 % 10
n3 = n % 10
res = n1 + n2 + n3

print(res)