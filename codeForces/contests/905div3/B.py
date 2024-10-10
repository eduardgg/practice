
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    s = input()
    l = n-k
    cjt = set()
    pars = 0
    for c in s:
        if c in cjt:
            cjt.remove(c)
            pars += 1
        else:
            cjt.add(c)

    print("YES" if pars >= l//2 else "NO")