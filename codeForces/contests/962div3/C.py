
for _ in range(int(input())):
    n, q = list(map(int, input().split()))
    a = input()
    b = input()
    da = [[0 for _ in range(26)]]
    db = [[0 for _ in range(26)]]
    for i in range(n):
        da.append([e for e in da[-1]])
        db.append([e for e in db[-1]])
        da[-1][ord(a[i]) - ord('a')] += 1
        db[-1][ord(b[i]) - ord('a')] += 1

    for _ in range(q):
        l, r = list(map(int, input().split()))
        eqs = 0
        for c in range(26):
            eqs += min(da[r][c] - da[l-1][c], db[r][c] - db[l-1][c])
        ans = r - l + 1 - eqs
        print(ans)