def a(n):
    x = 0
    if (n>0):
        x=n*a(n-1)
        print(n,x)
    else:
        return 1
    return x
y = int(input("type number>> "))
print(a(y))
