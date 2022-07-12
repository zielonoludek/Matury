dane1 = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\czerwiec_2018\\dane1.txt","r").read()
dane2 = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\czerwiec_2018\\dane2.txt","r").read()
odp = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\czerwiec_2018\\wyniki4.txt","w")

l1 = dane1.split("\n")
l2 = dane2.split("\n")

zad1 = 0
zad2 = 0

zad3 = []

zad4 = []

for i in range(len(l1)):

    ciag3 = []

    ciag1 = (l1[i]).split(" ")
    ciag2 = (l2[i]).split(" ")

    cyfry1, cyfry2 = [], []

    for j in range(len(ciag1)):

        if ciag1[j] != '' and ciag2[j] != '':
            ciag3.append(int(ciag1[j]))
            ciag3.append(int(ciag2[j]))

            if ciag1[j] not in cyfry1:
                cyfry1.append(ciag1[j])
            if ciag2[j] not in cyfry2:
                cyfry2.append(ciag2[j])

    if cyfry2 == cyfry1 and cyfry1 != [] and cyfry2 != [] :
        zad3.append(i+1)

    if ciag1[0] != '' and ciag2[0] != '' and (ciag1[9] == ciag2[9]):
        zad1 += 1

    p1 = 0
    p2 = 0

    for j in range(len(ciag1)):
        if ciag1[j] != '' and ciag2[j] != '':
            c1 = ciag1[j]
            c2 = ciag2[j]

            if (c1 != '') and (c2 != ''):

                if int(c2) % 2 == 0:
                    p2 += 1
                if int(c1) % 2 == 0:
                    p1 += 1

    if (p2 == 5) and (p1 == 5):
        zad2 += 1

    ciag3.sort()

    if ciag3 != []:
        zad4.append(ciag3)


print(f"zad 1: {zad1}\nzad 2: {zad2}\nzad3: {zad3}\nzad4:\n")

odp.write(f"zad 1: {zad1}\nzad 2: {zad2}\nzad 3 numery wierszy: {zad3}\nzadanie 4")

i = 1
for linia in zad4:
    if i <= 30:
        wers = ''
        for liczba in linia:
            wers += str(liczba)
            wers += ' '
        odp.write(f"\n{wers}")
    i+= 1

odp.close()


