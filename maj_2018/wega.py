file = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\maj_2018\\sygnaly.txt","r").read()

lines = file.split("\n")

przeslanie = ''
ile = 0
zad4 = []
word = ''
i = 1
for line in lines:
    if i % 40 == 0:
        przeslanie += line[9]
    i+=1

    slowo = list(line)

    tab = []
    pom = len(slowo)*(len(slowo)-1)

    for j in range(len(slowo)):
        for k in range(len(slowo)):
            if k != j and abs(ord(slowo[k]) - ord(slowo[j])) <= 10:
                pom -= 1

        if slowo[j] not in tab:
            tab.append(slowo[j])

    if len(tab) > ile:
        ile = len(tab)
        word = line

    if pom == 0:
        zad4.append(line)



print(f"1: {przeslanie}  \n2: {word}  {ile} \n3:")
for i in range(len(zad4)):
    print(zad4[i])
