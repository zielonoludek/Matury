def first(a):
    n = len(a)
    left = 0
    right = n-1
    war = True
    while war:
        mid = (left + right)//2
        if a[mid] %2 ==0:
            right = mid
        if a[mid] % 2 != 0:
            left = mid
        if left == n:
            war = False
    return right
tab = [5,99,3,7,111,13,4,24,6,8]
print(first(tab))