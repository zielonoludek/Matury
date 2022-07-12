def dlugosc(n):
    dl = 0
    pom = n
    while pom != 0:
        x = 0
        for i in range(n):
            if i*i> pom and x == 0:
                pom -= (i-1)*(i-1)
                dl += 1
                x = 1
    return dl

print(dlugosc(18))
