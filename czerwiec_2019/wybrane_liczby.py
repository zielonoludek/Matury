liczby = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\czerwiec_2019\\liczby.txt","r").read()
pierwsze = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\czerwiec_2019\\pierwsze.txt","r").read()

liczby = liczby.split("\n")
pierwsze = pierwsze.split("\n")

w1 = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\czerwiec_2019\\wyniki4_1.txt","w")
w2 = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\czerwiec_2019\\wyniki4_2.txt","w")
w3 = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\czerwiec_2019\\wyniki4_3.txt","w")


def pierwsza(n):
    for i in range(2,n):
        if n%i == 0:
            return False

    return True


def waga(n):
    suma = 0
    for i in range(len(n)):
        suma += int(n[i])
    if suma < 10:
        return suma
    return waga(str(suma))


z1 = []
z2 = []
z3 = 0

for liczba in liczby:
    if liczba != "":
        p1 = (pierwsza(int(liczba[::-1])))
        liczba = int(liczba)
        p = pierwsza(liczba)

        if (liczba >=100) and liczba <= 5000 and p:
            z1.append(liczba)


for liczba in pierwsze:
    if liczba != "":
        if waga(liczba) == 1:
            z3 += 1
        if pierwsza(int(liczba[::-1])):
            z2.append(liczba)

print(z1)
print(z2)
print(len(z2))
print(z3)

w1.close()
w2.close()
w3.close()