def pow(a,b):
    x = a
    if b == 0:
        return 1
    for i in range(b):
        a = a*x

    return a

def dopelnienie(n):
    x = 0
    for i in range(n):
        if pow(10,i)>n:
            x = pow(10,i)
            break
    x-= 1
    print(x)
    return (x-n)

print(dopelnienie(111111111))
