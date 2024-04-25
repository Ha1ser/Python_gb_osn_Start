# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

num = 5
num1 = 0
num2 = 1
num3 = 0
k = 1

while num3 < num:
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    k = k + 1
    print(num1, num2, num3)
    if num3 > num:
        k = -1
print(k)

