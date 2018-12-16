a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

def GCD(a, b):
    if a < b:
        temp = b
        b = a
        a = temp

    r = a%b
    if r == 0:
        return b
    else:
        return GCD(b,r)


print(GCD(a,b))


