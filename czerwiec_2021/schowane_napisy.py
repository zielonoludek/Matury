file = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\czerwiec_2021\\napisy.txt","r").read()
w = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\czerwiec_2021\\wyniki4.txt","w")

def number(x):
    if (ord(x)>=48) and (ord(x)<= 57):
        return True

def palindrom(n):
    x = n[0]
    a = n+x
    if a == a[::-1]:
        return a[25]
    x = n[49]
    n = x+n
    if n == n[::-1]:
        return n[25]
    return False

file = file.split("\n")
haslo = ''

ile_liczb = 0
abc = ''
last = 'ja'
pom = ''
ileX = 0

for line in file:
    if line != "":
        test = ''
        if palindrom(line) != False:
            abc += palindrom(line)
        for i in range(len(line)):
            if number(line[i]):
                ile_liczb += 1
                test += line[i]
        if len(test) != 0:
            for i in range(len(test)):
                if i%2 != 0:
                    num = int(test[i-1]+test[i])
                    if num > 65 and num < 90:
                        pom += chr(num)
                        if chr(num) == 'X':
                            ileX += 1
                            if ileX == 3:
                                last = pom
                                break

n = 0
for i in range(len(file)):
    if file[i] != "":
        if (i+1)%20 == 0:
            haslo += file[i][n]
            n+= 1


w.close()
print(ile_liczb)
print(haslo)
print(abc)
print(last)

