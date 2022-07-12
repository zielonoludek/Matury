def odd(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True


def parzysta(n):
    if n%2==0:
        return True
    return False

def gold(n):
    if n <= 4:
        return n
    tab = []
    roz = -1
    for i in range(2,n-1):
        if odd(i) and odd(n-i):
            x = abs(n - i)
            if abs(n-i-i) > roz:
                roz = abs(n-i-i)
                tab = [i, n-i]
    tab.sort()
    return tab

def dwa(a):
    a = list(a)
    dlugosc = 0
    pom = 1
    one = 0
    last = 0

    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            pom += 1
        else:
            if pom>dlugosc:
                dlugosc = pom
                last = i+1
                one = last - pom
                pom = 1

        if i+1 == len(a)-1:
            if pom > dlugosc:
                dlugosc = pom
                last = i + 2
                one = last - pom
                pom = 1
    a = "".join(a[one:last])
    return (a)


file = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\maj_2020\\pary.txt","r").read()
wynik = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\maj_2020\\wyniki4.txt","w")

wynik.write('4.1\n')
file = file.split("\n")
zad_2 = []

for line in file:
    if line != "":
        line = line.split(" ")
        num = int(line[0])
        word = line[1]
        if parzysta(num):
            tab = gold(num)
            wynik.write(f"{num} {tab[0]} {tab[1]}\n")
        a = dwa(word)
        zad_2.append(f"{a} {len(a)}")

zad3 = ''
w = [100000000000, 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz']

for i in range(len(file)):
    for j in range(len(file)):
        if file[i] != '' and file[j] != '' and j!=i:
             a = file[i].split(" ")
             b = file[j].split(" ")
             l1 = int(a[0])
             w1 = a[1]
             l2 = int(b[0])
             w2 = b[1]
             if (l1 < l2) or ((l1 == l2) and (w1 < w2)):
                 if l1 == len(w1):

                    if (l1 < w[0]) or ((l1 == int(w[0])) and (w1 < w[1])):
                        w = [l1,w1]
wynik.write('\n\n4.2\n\n')
for i in range(len(zad_2)):
    wynik.write(f"{zad_2[i]}\n")

wynik.write('\n\n\n4.3\n\n')
wynik.write(f"{w[0]} {w[1]}")

wynik.close()











