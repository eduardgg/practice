
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    top = 0
    suma = 0
    ans = 0
    for e in a:
        top = max(top, e)
        suma += e
        if top*2 == suma:
            ans += 1
    print(ans)