
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    els = set()
    suma = 0
    ans = 0
    for e in a:
        suma += e
        els.add(e)
        ans += (not suma%2 and suma//2 in els)
    print(ans)