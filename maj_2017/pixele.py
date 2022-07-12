f = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\maj_2017\\dane.txt","r").read()
f = f.split("\n")


def kontrast(x,y):
    if abs(x-y)> 128:
        return True
    return False


light = 0
dark = 255
z2 = 0
for line in range(len(f)):
    if f[line] != "":
        line = f[line].split(" ")
        xline = line[::-1]
        p = 0

        for i in range(len(line)):
            if xline[i] != line[i] and p == 0:
                z2 += 1
                p += 1
            pixel = int(line[i])
            if pixel > light:
                light = pixel
            if pixel < dark:
                dark = pixel
tab = []
for l in range(len(f)-1):
    if f[l] != "":
        f[l] = f[l].split(" ")
        tab.append(f[l])

z3 = 0

for i in range(1, len(f)-2):
    if f[i] != "":
        for j in range(1,len(f[i])-1):
            x = int(f[i][j])
            y = int(f[i][j+1])
            z = int(f[i+1][j])
            a = int(f[i][j-1])
            b = int(f[i-1][j])
            if kontrast(x,y) or kontrast(x,z) or kontrast(x,a) or kontrast(x,b):
                z3 += 1

maxi = 0

for j in range(320):
    ile = 1
    for i in range(199):
        x = int(tab[i][j])
        y = int(tab[i+1][j])
        if x != y:
            if ile > maxi:
                maxi = ile
            ile = 1
        else :
            ile += 1





print(light, dark, z2, z3, maxi)
