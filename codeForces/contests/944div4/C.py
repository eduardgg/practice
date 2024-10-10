
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    a,b,c,d = line()
    v = [a,b,c,d]
    v.sort()
    ind = []
    for i in range(4):
        if v[i] in {a, b}:
            ind.append(i)
    if ind[1] - ind[0] == 2:
        print("YES")
    else:
        print("NO")