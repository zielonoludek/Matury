def czy(a):
    sumaA = 0
    for i in range(1,a-1):
        if a%i==0:
            sumaA+=i
    b = sumaA-1
    sumaB =0
    for i in range(1,b-1):
        if b%i==0:
            sumaB+=i
    if sumaB -1 ==a:
        return b

    return 'NIE'

print(czy(75))