
for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    a = [b[0]]
    for i in range(n-2):
        a.append(b[i] | b[i+1])
    a.append(b[-1])
    ok = True
    for i in range(n-1):
        if a[i] & a[i+1] != b[i]:
            ok = False
            break
    if ok:
        print(*a)
    else:
        print(-1)