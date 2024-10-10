
line = lambda : list(map(int, input().split()))
 
for _ in range(int(input())):
    n, q = line()
    c = line()
    uns = [0]*(n+1)
    sumes = [0]*(n+1)
    for i in range(n):
        sumes[i+1] = sumes[i] + c[i]
        uns[i+1] = uns[i] + (c[i] == 1)
 
    for _ in range(q):
        l, r = line()
        if l == r:
            print("NO")
            continue
        un = uns[r] - uns[l-1]
        suma = sumes[r] - sumes[l-1]
        q = r-l+1
        if q + un > suma:
            print("NO")
        else:
            print("YES")   