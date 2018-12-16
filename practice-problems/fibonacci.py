n = int(input("Enter the value of n:"))

def fib(x):
    if x==0:
        return 0
    elif x==1:
        return 0
    elif x==2:
        return 1
    else :
        return fib(x-2) + fib(x-1)



for i in range(1,n+1):
    print(fib(i))


