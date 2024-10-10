
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = []
    d = {}
    for i in range(n):
        if a[i] not in d.keys():
            d[a[i]] = i
        b.append(d[a[i]])

    notp = (len(d.keys()) > 26)
    m = int(input())
    for _ in range(m):
        s = input()
        if len(s) != n or notp:
            print("NO")
            continue
        
        d = [-1]*26
        ok = True
        for i in range(n):
            if d[ord(s[i])-ord('a')] == -1:
                d[ord(s[i])-ord('a')] = i
            if d[ord(s[i])-ord('a')] != b[i]:
                ok = False
                break

        print("YES" if ok else "NO")