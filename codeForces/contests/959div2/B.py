
for _ in range(int(input())):
    n = int(input())
    s = input()
    t = input()
    ok = True
    for i in range(n):
        if s[i] == '1':
            break
        elif t[i] == '1':
            ok = False
            break
    print("YES" if ok else "NO")