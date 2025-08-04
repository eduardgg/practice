
n = int(input())
obj = (n**2)//2
l, r = 1, n**2
# l: la més petita trobada que funciona
# r: la més petita trobada que no funciona
while r-l > 1:
    m = (r+l)//2
    trobat = 0
    less = 0
    for i in range(1, n+1):
        less += min(m//i, n)
        if m%i == 0 and m//i <= n:
            trobat += 1
    if less-trobat > obj:
        r = m
    elif less <= obj:
        l = m+1
    else:
        l = m
        break
print(l)