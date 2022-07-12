main = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\marzec_2021\\galerie.txt","r").read()
w1 = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\marzec_2021\\wynik4_1.txt","w")
w2 = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\marzec_2021\\wynik4_2a.txt","w")
w3 = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\marzec_2021\\wynik4_2b.txt","w")
w4 = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\marzec_2021\\wynik4_3.txt","w")

print(main)
main = main.split("\n")
print(main)

miasta = []
maxi = 0
mini = 1000000000000
m_mini = ''
m_maxi = ''
ile_lok_max = 0
ile_lok_min = 1000000000000000000000000000000
m_lok_max = ''
m_lok_min = ''

for line in main:
    if line != "":
        line = line.split(" ")
        if line[0] not in miasta:
            miasta.append(line[0])
            miasta.append(1)
        else:
            for i in range(len(miasta)):
                if miasta[i] == line[0]:
                    miasta[i+1] += 1
        pole = 0
        ile = 0
        pom = []
        for i in range(len(line)):
            if i % 2 == 0:
                if line[i] != "0" and ord(line[i][0]) < 65:
                    sqr = int(line[i])*int(line[i+1])
                    pole += sqr
                    if sqr not in pom:
                        pom.append(sqr)
                    ile += 1

        if len(pom) > ile_lok_max:
            ile_lok_max = len(pom)
            m_lok_max = line[1]
        if len(pom) < ile_lok_min:
            ile_lok_min = len(pom)
            m_lok_min = line[1]

        if pole < mini:
            mini = pole
            m_mini = line[1]
        if pole > maxi:
            maxi = pole
            m_maxi = line[1]
        w2.write(f"{line[1]} {pole} {ile}\n")

w4.write(f"{m_lok_max} {ile_lok_max}\n{m_lok_min} {ile_lok_min}")

w3.write(f"{m_maxi} {maxi}\n{m_mini} {mini}")

for i in range(len(miasta)):
    if i%2 == 0:
        w1.write(f"{miasta[i]} {miasta[i+1]}\n")

w1.close()
w2.close()
w3.close()
w4.close()