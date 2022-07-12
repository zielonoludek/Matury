file = open("C:\\Users\\marty\\OneDrive\Dokumenty\\matura_infa\\czerwiec_2016\\liczby.txt","r").read()

file = file.split("\n")


def zamiana(n, a):
    x = 0
    a = int(a)
    for i in range(len(n)):
        x += (a**i)*int(n[i])
    return x


zad1 = 0
zad2 = 0
zad3 = 0
zad4 = 0
l_max = ''
l_min = ''
maxi = 0
mini = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

for num in file:
    if num != "":
        num = num[::-1]
        liczba = num[1::]
        podstawa = num[0]
        dec = zamiana(liczba, podstawa)

        if dec > maxi:
            maxi = dec
            l_max = num[::-1]

        if dec < mini:
            mini = dec
            l_min = num[::-1]

        if num[0] == "8":
            zad1 += 1
            zad4 += dec

        if (podstawa == "4") and ("0" not in liczba):
            zad2 += 1

        if (podstawa == "2") and (liczba[0] == "0"):
            zad3 += 1

        liczba = liczba[::-1]


print(zad1)
print(zad2)
print(zad3)
print(zad4)
print(f"{l_min}, {mini}\n{l_max}, {maxi}")


