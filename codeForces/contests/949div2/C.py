
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    l = 0
    while l < n and a[l] == -1: l += 1
    
    for i in range(l-1, -1, -1):
        if i == n-1: a[i] = 1
        elif a[i+1] > 1: a[i] = a[i+1]//2
        else: a[i] = 2*a[i+1]

    while l < n:
        r = l+1
        if r >= n or a[r] != -1:
            l = r
            continue
        while r < n and a[r] == -1: r += 1

        if r == n:
            for j in range(l+1, n):
                if a[j-1] > 1: a[j] = a[j-1]//2
                else: a[j] = 2*a[j-1]
            break

        br = a[r].bit_length()
        bl = a[l].bit_length()

        if ((br-bl)-(r-l)) % 2 or br-bl > r-l or bl-br > r-l: break
        x = ((r-l)-(br-bl))//2
        for i in range(min(x, r-l-1)):
            if a[l+i] > 1: a[l+i+1] = a[l+i]//2
            else: a[l+i+1] = 2*a[l+i]
        for i in range(r-l-x-1):
            if a[r-i] > 1: a[r-i-1] = a[r-i]//2
            else: a[r-i-1] = 2*a[r-i]

        l = r

    # Final check
    ok = True
    if a[0] < 1 or a[0] > 10**9:
        ok = False
    for i in range(1, n):
        if a[i] < 1 or a[i] > 10**9 or (a[i]//2 != a[i-1] and a[i-1]//2 != a[i]):
            ok = False
            break
    
    if not ok: print(-1)
    else: print(*a)