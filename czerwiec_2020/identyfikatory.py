def proper(num, text):
    test = num[0]
    sum = 0
    sum += (ord(txt[0]) - 55) * 7
    sum += (ord(txt[1]) - 55) * 3
    sum += (ord(txt[2]) - 55)

    sum += int(num[1]) * 7
    sum += int(num[2]) * 3
    sum += int(num[3]) * 1
    sum += int(num[4]) * 7
    sum += int(num[5]) * 3

    if sum % 10 == int(test):
        return True
    return False


file = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\czerwiec_2020\\identyfikator.txt","r").read()

file = file.split("\n")

z1 = []
maks_1 = 0
maks = 0
zad2 = []
zad3 = []

for line in file:
    if line != "":
        num = line[3::]
        txt = line[0:3]
        if proper(num, txt) == False:
            zad3.append(line)
        if txt == txt[::-1] or num == num[::-1]:
            zad2.append(line)
        sum = 0
        for i in range(len(num)):
            sum+= int(num[i])
        if sum > maks:
            maks = sum
            z1 =[]
            z1.append(line)
        elif sum == maks:
            z1.append(line)

print(z1)
print(zad2)
print(zad3)