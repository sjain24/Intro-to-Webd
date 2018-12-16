n = int(input("Enter number of elements in list:"))
a =[]
for i in range(n):
    a.append(input(""))

def abbr(B,lenB):
    for i in range(lenB):
         print( B[i][0] , end="")
    print("")
    return


for j in range(n):
    b = a[j].split()
    abbr(b,len(b))