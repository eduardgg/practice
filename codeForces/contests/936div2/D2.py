
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, x = line()
    a = line()
    xor = 0
    b = x.bit_length()
    for e in a:
        b = max(b, e.bit_length())
        xor ^= e
    if xor > x:
        print(-1)
        continue
    
    unions = 0
    comps = n
    top = 1
    nxt = [i+1 for i in range(n)]
    ok = True

    while b >= 0:

        if x & (1 << b):
            primer = False
            unions = 0
            i = 0
            while i < n:
                if (a[i] & (1 << b)):
                    if not primer:
                        primer = True
                        unions += 1
                    else:
                        primer = False
                elif primer:
                    unions += 1
                i = nxt[i]
            top = max(top, comps-unions)
            if comps <= top:
                break

        else:
            primer = False
            i = 0
            while i < n:
                if (a[i] & (1 << b)):
                    if not primer:
                        primer = True
                        pri = i
                    else:
                        primer = False
                        nxt[pri] = nxt[i]
                        a[pri] ^= a[i]
                        comps -= 1
                elif primer:
                    nxt[pri] = nxt[i]
                    a[pri] ^= a[i]
                    comps -= 1
                i = nxt[i]
            if primer:
                ok = False
                break

        b -= 1

    if ok:
        top = max(top, comps)
    print(top)