
# Funciona, però no és eficient
# Cal crear una bilinked list -> C2

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    c = list(map(int, input().split()))
    l.sort()
    r.sort()
    
    ints = []
    posl = 0
    for i in range(len(r)):
        if posl < len(l) and l[posl] >= r[i]:
            posl -= 1
        while posl < len(l) and l[posl] < r[i]:
            posl += 1
        posl -= 1
        ints += [r[i] - l.pop(posl)]
    
    ints.sort()
    c.sort()
    cost = 0
    for i in range(len(c)):
        cost += c[i]*ints[-1-i]
    print(cost)