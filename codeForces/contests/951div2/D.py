
for _ in range(int(input())):

    n, k = list(map(int, input().split()))
    s = input()

    c = s[0]
    i = 1
    l = 1
    ans = None
    while i < n:
        if s[i] == s[i-1]:
            l += 1
            if l > 2*k: break
        else:
            if l < k:
                s = s[i:] + s[:i][::-1]
                ans = i
                break
            elif k < l:
                s = s[i-k:] + s[:i-k][::-1]
                ans = i-k
                break
            l = 1
        i += 1

    # print(s)
    c = s[0]
    i = 0
    ok = True
    while i < n:
        if s[i] != c:
            ok = False
            break
        if not (i+1)%k:
            c = str(1-int(c))
        i += 1

    if ok and ans == None:
        if n == k: ans = 1
        elif s[-1] == s[0]: ans = 2*k
        else: ans = k

    print(ans if ok else -1)