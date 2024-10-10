
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    for _ in range(m):
        d1, d2 = {}, {}
        s = input()
        if len(s) != n:
            print("NO")
            continue
        ok = True
        for j in range(n):
            if (s[j] in d1) ^ (a[j] in d2):
                ok = False
                break
            elif s[j] in d1:
                if d1[s[j]] != a[j] or d2[a[j]] != s[j]:
                    ok = False
                    break
            else:
                d1[s[j]] = a[j]
                d2[a[j]] = s[j]
        print("YES" if ok else "NO")