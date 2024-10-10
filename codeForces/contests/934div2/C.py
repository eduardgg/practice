
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    v = [0]*n
    for e in a:
        v[e] += 1
    if v[0] == 0:
        print(0)
        continue
    while v[-1] == 0:
        v.pop()
    
    primer = False
    ok = False
    for i in range(len(v)):
        if v[i] == 0:
            mex = i
            ok = True
            break
        elif v[i] == 1:
            if primer:
                mex = i
                ok = True
                break
            primer = True
    if ok:
        print(mex)
    else:
        print(len(v))