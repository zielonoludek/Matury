d = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\matura_infa\\marzec_2021\\bloki2.txt","r").read()

d = d.split("\n")

d = d[::-1]
d = d[1::]
d = d[::-1]

for x in range(len(d)):
    d[x] = int(d[x])

max = 0

for i in range(len(d)):
    for j in range(i+1,len(d)):
        if (sum(d[i::j]))% 3 == 0:
            length = j-i
            if length>max:
                max = length+1

print(max)