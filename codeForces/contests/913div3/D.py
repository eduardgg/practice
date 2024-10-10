
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    ls, rs = [], []
    for i in range(n):
        l, r = line()
        ls.append(l)
        rs.append(r)
    
    # Binary Search:
    # mink és l'últim valor amb el que sabem que NO es pot
    # maxk és el primer valor amb el que sabem que SÍ es pot
    # Iterem mentre maxk - mink > 1, i el resultat serà maxk
    mink, maxk = -1, 10**9
    while maxk - mink > 1:
        k = (mink + maxk) // 2
        seg = [0, 0]
        ok = True
        for i in range(n):
            if seg[1]+k < ls[i] or seg[0]-k > rs[i]:
                mink = k
                ok = False
                break
            seg = [max(seg[0]-k, ls[i]), min(seg[1]+k, rs[i])]
        if ok:
            maxk = k
    
    print(maxk)