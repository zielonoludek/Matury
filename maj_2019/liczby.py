import random

file = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\maj_2019\\liczby.txt","r").read()

file = file.split("\n")


def silnia(n):
    if n == 0:
        return 1
    return silnia(n-1)*n


def threepow(n):
    for i in range(11):
        if 3**i == n:
            return True


def NWD(n,m):
    if m < n:
        m,n = n,m
    for i in range(1, n+1):
        if n%i == 0 and m%i == 0:
            x = i
    return x

zad1 = 0
zad2 =[]
for num in file:
    if num != '':
        array = list(num)
        liczba = int(num)

    suma = 0
    for x in array:
        suma += silnia(int(x))

    if suma == liczba:
        zad2.append(liczba)
    if threepow(liczba):
        zad1 += 1

pom = []
tab = []
dpom = 0
first = ''
dzielnik = 1
dlugosc = 0
for i in range(1, len(file)):
    if file[i] != '' :
        n1 = int(file[i-1])
        n2 = int(file[i])

        if pom == []:
            pom.append(n1)

        d = NWD(pom[len(pom)-1], n2)
        if (d > 1) and (d == NWD(n1,n2)):
            dpom = d
            pom.append(n2)
        else :
            if len(pom) >= dlugosc and len(pom) > 1:
                pom = pom[0:len(pom)-1]
                dlugosc = len(pom)
                dzielnik = dpom
                first = pom[0]

            pom = []


print(f"{first, dlugosc, dzielnik}")

print(f"zad 1: {zad1}\n zad 2: {zad2}\n")



