def f(n):
    if n == 0:
        return 1
    s = 1
    for i in range(n):
        s+= f(i)

    return s

print(f(200))
