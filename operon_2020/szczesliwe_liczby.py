file = open("dane.txt","r").read()
file = file.split("\n")

def d(tab,a):
    i = 0
    pom = 1
    war = True
    while war:
        if pom == a:
            del(tab[i])
            pom = 0
        pom += 1
        i +=1
        if i+1 >= len(tab):
            war = False
    return tab

lucky = []
for i in range(1,10001):
    if i%2 != 0:
        lucky.append(i)

i = 0
war = True
while war:
    if lucky[i] != 1:
        lucky = d(lucky, lucky[i])
    i += 1
    if i+1 >= len(lucky):
        war = False

print(lucky)