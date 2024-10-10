
def dp(mex):
    if M[mex] != -1:
        return M[mex]
    if mex == 0:
        return 0
    minim = float('inf')
    for k in d.keys():
        if k >= mex:
            break
        cost = (d[k]-1)*mex + k + dp(k)
        if cost < minim:
            minim = cost
    M[mex] = minim
    return M[mex]

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    if a[0] != 0:
        print(0)
        continue

    d = {}
    for ai in a:
        d[ai] = d.get(ai, 0) + 1

    mex = 0
    for k in d.keys():
        if k > mex:
            continue
        elif k == mex:
            mex += 1
            
    M = [-1 for _ in range(mex+1)]
    print(dp(mex))