t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    s = input()
    t = input()
    
    goodT0 = False
    goodT1 = False
    if t[0] == t[-1]:
        goodT = True
        for i in range(m-1):
            if t[i] == t[i+1]:
                goodT = False
                break
        if goodT:
            if t[0] == '0':
                goodT0 = True
            else:
                goodT1 = True
    
    ok = True
    for i in range(n-1):
        if s[i] == s[i+1]:
            if s[i] == '0' and not goodT1:
                ok = False
                break
            elif s[i] == '1' and not goodT0:
                ok = False
                break

    if ok:
        print("YES")
    else:
        print("NO")