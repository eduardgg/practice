
for _ in range(int(input())):

    n, m, k = list(map(int, input().split()))
    d, a = list(map(int, input().split()))
    n -= 1
    i = 1
    ans = 0
    stack = []

    while n or i - d < k:
        
        if i == d:
            stack.append((d, a))
            if n:
                d, a = map(int, input().split())
                n -= 1
        
        mc = m
        b = False
        while stack:
            dn, an = stack.pop()
            if i - dn >= k:
                stack = []
                break
            if an >= mc:
                ans += 1
                i += 1
                b = True
                an -= mc
                incr = max(0, min(an//m, dn + k - i, d - i))
                ans += incr
                i += incr
                an -= incr*m
                stack.append((dn, an))
                break
            else:
                mc -= an

        if not b:
            i = max(i+1, d)
    
    print(ans)