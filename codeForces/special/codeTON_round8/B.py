
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    
    mex = n
    p = []
    for e in a[::-1]:
        p.append(mex-e)
        mex = min(mex, p[-1])
    p = p[::-1]
    print(*p)