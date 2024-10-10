
p = int(input())
for _ in range(p):
    n = int(input())
    s = input()
    t = input()
    q = int(input())

    tt = [t[0]] + ['1' if s[i-1] == s[i+1] == '0' else t[i] for i in range(1, n-1)] + [t[-1]]
    ts = [s[0]] + ['1' if tt[i-1] == tt[i+1] == '1' else s[i] for i in range(1, n-1)] + [s[-1]]
    uns = [0]
    for c in ts: uns.append(uns[-1] + (c == '1'))
    for _ in range(q):
        l, r = list(map(int, input().split()))
        if r-l == 0: ans = int(s[l-1])
        elif r-l == 1: ans = int(s[l-1]) + int(s[r-1])
        elif r-l == 2: ans = int(s[l-1]) + int(s[r-1]) + int(s[l] == '1' or (t[l-1] == '1' and t[r-1] == '1'))
        else:
            ans = uns[r-2] - uns[l+1]
            if s[l-1] == '1': ans += 1
            if s[r-1] == '1': ans += 1
            if s[l] == '1' or (t[l-1] == '1' and (t[l+1] == '1' or s[l+2] == '0')): ans += 1
            if s[r-2] == '1' or (t[r-1] == '1' and (t[r-3] == '1' or s[r-4] == '0')): ans += 1

        print(ans)