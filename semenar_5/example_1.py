# найти факториал с помощью рекурсии...

num = 5

def fact(n):
    if n < 1:
        return 1
    print(n)
    return n * fact(n - 1)


print(fact(num))