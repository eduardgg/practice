
for _ in range(int(input())):
    n = int(input())
    s = input()
    nn = s.count('N')
    ns = s.count('S')
    ne = s.count('E')
    nw = s.count('W')
    if (nn-ns)%2 or (ne-nw)%2 or (nn, ns, ne, nw) in {(1,1,0,0),(0,0,1,1)}:
        print("NO")
        continue
    
    dir = {"N": True, "S":True, "E":False, "W":False}
    for d in s:
        if dir[d]: print("R", end="")
        else: print("H", end="")
        dir[d] = not dir[d]

    print()