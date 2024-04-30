a = "512315"
def f(a):
    if len(a) < 2:
        return True
    elif  a[0] == a[-1]:
        return f(a[1: -1])
    else:
        return False

print(f(a))

