z1 = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\maj_2016\\dane_6_1.txt","r").read()

def szyfr(n):
    n = list(n)
    k = 107
    for i in range(len(n)):
        x = ord(n[i])
        while x + k > 90:
           k = k + n -
        n[i] = chr(x)
    return "".join(n)


lines = z1.split("\n")
for line in lines:
    print(szyfr(line))