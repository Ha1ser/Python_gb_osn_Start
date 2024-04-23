# флаг тоже самое что и break, но break является правилом плохого тона в ооп, поэтому лучше использовать flag

n = int(input())
flag = True 
i = 2
while flag:
    if n % i == 0:
        flag = False
        print(i)
    elif i > n // 2:
        print(n)
        flag = False
    i += 1
    