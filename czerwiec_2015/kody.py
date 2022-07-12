file = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\czerwiec_2015\\kody.txt","r").read()
w1 = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\czerwiec_2015\\kody1.txt","w")
w2 = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\czerwiec_2015\\kody2.txt","w")
w3 = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\czerwiec_2015\\kody3.txt","w")
kod = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\czerwiec_2015\\cyfra_kodkreskowy.txt","r").read()

file = file.split("\n")
kod = kod.split("\n")
kod = kod[1::]

for i in range(len(kod)):
    kod[i]= kod[i].split("\t")
    kod[i] = kod[i][1]



def even(n):
    s = 0
    for i in range(len(n)):
        if (i+1)%2 == 0:
            s+= int(n[i])
    return s


def odd(n):
    s = 0
    for i in range(len(n)):
        if (i+1)%2 != 0:
            s+= int(n[i])
    return s


def contol(n):

    return str((10-(odd(n) + 3*even(n))%10)%10)


def code(n):
    start = '11011010'
    stop = '11010110'
    c = start
    for i in range(len(n)):
        c+= kod[int(n[i])]
    c += kod[int(contol(n))]
    c += stop
    return c



for num in file:
    sodd = odd(num)
    seven = even(num)
    x = int(contol(num))
    w1.write(f"{seven} {sodd}\n")
    w2.write(f"{kod[x]} {x}\n")
    w3.write(f"{code(num)}\n")

w1.close()
w2.close()
w3.close()

