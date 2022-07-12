#zczytuje plik
file = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\czerwiec_2017\\punkty.txt", "r").read()


#funkcja która sprawdza czy n jest liczbą pierwszą
def pierwsza(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


#funkcja, która zwraca nam odległość punktu a od b
def odleglosc(a, b):
    xa = int(a[0])
    ya = int(a[1])
    xb = int(b[0])
    yb = int(b[1])

    return round(((xb - xa)**2 + (yb - ya)**2)**0.5)


lines = file.split('\n')    # wsadzam dane do tablicy - arrayki, każda linijka jest oddzielona przecinkiem od siebie
#każda linijka zawiera współrzene jednego punktu, oddzielone spacją

zad_1 = 0       #wynik do podpunktu 1

zad_2 = 0

zad_3 = []      #arrayka do przechowania pary najbardziej oddlonych punktów
z3_odl = 0      #jaka jest odległosc tych punktów

wew = 0     #ile jest punktów wewnątrz kwadratu
bok = 0     # ile na boku
zew = 0     # ile w srodku


for line in lines:
    n = line.split(" ") # w każdej linijce są dwie współrzędne, dzielimy je na kolejną arraykę dwy elementową

    # wyciągamy współrzędne z arayki i zapisujemy do zmiennych
    x = n[0]
    y = n[1]

    # sprawdzamy czy obie współrzędne są liczbami pierwszymi
    if pierwsza(int(x)) and pierwsza(int(y)):
        zad_1 += 1


    #zadanie 2

    # jako, że każda współrzędna jest zczytana z pliku jest traktowana jako tekst,
    # mogę rozdzielić ją na pojedyńcze znaki i dać do arrayki

    x = list(x)
    y = list(y)

    # tablice pomocnicze, muszę sprawdzić czu obie współrzędne są zapisane za pomocą
    # tych samych cyfr, więc nie chcę mieć powtórzeń
    pomx = []
    pomy = []


    #dodaje elementy do arrayek, tak aby cyfry się nie powtarzały
    for i in x:
        if i not in pomx:
            pomx.append(i)

    for i in y:
        if i not in pomy:
            pomy.append(i)

    # sortuję arrayki, aby było je łatwo porównać
    pomx.sort()
    pomy.sort()

    #sprwadzam czy obie współrzędne są podobne do siebie --> są zapisane za pomocą tych samych cyfr
    if pomx == pomy:
        zad_2 += 1


for i in range(len(lines)):  # iterujemy linijki po koleji, przechodzimu przez każdy punkt
    a = lines[i].split(" ")  # w każdej linijce są dwie współrzędne, dzielimy je na kolejną arraykę dwu elementową

    # wyciągamy współrzędne z arayki i zapisujemy do zmiennych
    x = int(a[0])
    y = int(a[1])

    # zad 4 --> sprawdzamy gdzie punkt jest względem kwadratu 1000x1000 ze środkiem symetri w punkcie (0,0)
    if y == 5000 or x == 5000 or y == -5000 or x == -5000:
        bok += 1
    elif ((x < 5000) and (x > -5000)) and ((y > -5000) and (y < 5000)):
        wew += 1
    else:
        zew += 1

    # pętla w pętli jeszcze raz lecimy wszystkie punkty po kolei, aby porównać wszystkie ze sobą
    for j in range(len(lines)):
        b = lines[j].split(" ")
        if z3_odl < odleglosc(a, b):
            zad_3 = [a, b]
            z3_odl = odleglosc(a, b)


# wyświetlam na ekranie wyniki obliczeń
print(f"1: {zad_1} \n2: {zad_2} \n3: \npunkty: {zad_3} \nodległość między nimi: {z3_odl} \n4: \nwewnątrz kwadratu : {wew}\n na boku kwadratu: {bok}\n na zewnątrz kwadratu: { zew}")