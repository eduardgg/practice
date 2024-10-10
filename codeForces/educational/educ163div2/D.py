for t in range(int(input())):
    s = input()
    n = len(s)
    ok = False
    m = 0
    for k in range(n//2, 0, -1):
        m = 0
        for i in range(n-k):
            if '?' != s[i] != s[k+i] != '?':
                m = 0
            else:
                m += 1
                if m == k:
                    ok = True
                    break
        if ok:
            break
    print(2*m)