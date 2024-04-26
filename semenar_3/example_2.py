# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]

p = [1, 2, 3, 4, 5]
k = 4
k = k % len(p)       # делать остаток от деления(%) на большее значение, то останится тоже самое значение: 4 % 5 == 4... В данном случае оптимизирует код 
i = 0
a = 0
v = 0
while i < k:
    a = p.pop()
    v = p.insert(0, a)
    i += 1
print(p) 



