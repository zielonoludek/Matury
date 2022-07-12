def BinToDec(n):
    n = n[::-1]
    dec = 0
    for i in range(len(n)):
        dec += int(n[i]) * 2**i
    return dec


file = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\maj_2015\\liczby.txt","r").read()

line = file.split('\n')
zad41 = 0
zad43 = ['','']
two = 0
eight = 0
help = []
nLine = 0

for number in line:
    help.append(BinToDec(number))

minV = min(help)
maxV = max(help)

for number in line:
    nLine += 1
    zero = 0
    one = 0
    for i in range(len(number)):
        if number[i] == '0':
            zero += 1
        else:
            one += 1
    if BinToDec(number) == minV:
        zad43[0] = nLine
    elif BinToDec(number) == maxV:
        zad43[1] = nLine


    if zero > one:
        zad41 += 1

    number = number[::-1]
    if number[0] == '0':
        two += 1
    if number[0:3] == '000':
        eight += 1

minV = min(help)
maxV = max(help)

print(zad41)
print(two)
print(eight)
print(zad43)
