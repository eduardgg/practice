
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    p = line()
    freq = {}
    els = set()
    mex = 0
    top = 0
    for e in p:
        els.add(e)
        while mex in els:
            mex += 1
        freq[mex] = freq.get(mex, 0) + 1
        top += mex

    cyc = top
    for e in p:
        for k in list(freq.keys()):
            if k > e:
                freq[e] = freq.get(e, 0) + freq[k]
                cyc -= freq[k]*(k-e)
                freq.pop(k)
        freq[n] = 1
        if e > 0: freq[0] -= 1
        cyc += n
        # print(freq, cyc)
        top = max(top, cyc)
    
    print(top)

