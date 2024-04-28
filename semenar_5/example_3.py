num = 25

def number(n, dl = 2):
    if n == 2 or dl * dl > num:
        return "yes"
    elif n % dl == 0:
        return "no"
    return number(n, dl + 1)
    

print(number(num))