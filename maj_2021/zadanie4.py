plik = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\maj_2021\\instrukcje.txt", "r").read()


def dopisz(txt, c):
    return txt + c


def zmien(txt, c):
    return txt[:len(txt) - 1]+c


def usun(txt):
    return txt[:len(txt) - 1]


def przesun(txt, c):
    index = txt.find(c)
    if index == -1:
        return txt

    if c == 'Z':
        c = 'A'
    else:
        c = chr(ord(c) + 1)
    txtlist = list(txt)
    txtlist[index] = c
    return "".join(txtlist)


tab = []
for i in range(ord('Z')+1):
    tab.append(0)

txt = ''
all = plik.split('\n')
ciag = 1
pom = 0
w2 = 0
w2i = 0

for wers in all:
    ins = wers.split(' ')
    if ins[0] == 'ZMIEN':
        txt = zmien(txt, ins[1])
    if ins[0] == 'DOPISZ':
        txt = dopisz(txt, ins[1])
        tab[ord(ins[1])] += 1

    if ins[0] == 'USUN':
        txt = usun(txt)
    if ins[0] == 'PRZESUN':
        txt = przesun(txt, ins[1])

z3 = ''
maxi = max(tab)
for i in range(len(tab)):
    if tab[i] == max(tab):
        z3 = chr(i)

previous = 'DOPISZ'
for i in range(len(all)):
    ins = all[i].split(' ')

    if ins[0] == previous:
        pom = previous
        ciag += 1
        if i != len(all)-1:
            next = all[i+1].split(' ')
            if ciag >= w2 and ins[0] != next[0]:
                w2 = ciag
                w2i = pom
        else:
            if ciag >= w2:
                w2 = ciag
                w2i = pom
    else:
        ciag = 1
    previous = ins[0]

print(len(txt))

print(w2i)
print(w2)

print(z3)
print(maxi)

print(txt)