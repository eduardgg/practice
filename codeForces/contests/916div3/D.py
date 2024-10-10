
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    b = line()
    c = line()
    aa = [(a[i], i) for i in range(n)]
    bb = [(b[i], i) for i in range(n)]
    cc = [(c[i], i) for i in range(n)]
    aa.sort()
    bb.sort()
    cc.sort()
    a = aa[n-3:]
    b = bb[n-3:]
    c = cc[n-3:]
    top = 0
    for (ea, i) in a:
        for (eb, j) in b:
            for (ec, k) in c:
                if i != j != k != i:
                    top = max(top, ea+eb+ec)
    print(top)