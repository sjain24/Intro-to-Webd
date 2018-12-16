n = list(input("Enter your number:"))

def insert_comma(n, i):
    n.insert(-3 - i, ',')
    i = i + 4
    if i +3 <= len(n)-1:
        insert_comma(n, i)
    else: return


if len(n) >= 3:
    insert_comma(n, 0)
    print(''.join(n))
else:
    print(''.join(n))