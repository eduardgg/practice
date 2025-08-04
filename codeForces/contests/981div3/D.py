
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = {0}
    suma = 0
    ans = 0
    for e in a:
        suma += e
        if suma in s:
            ans += 1
            suma = 0
            s = {0}
        else:
            s.add(suma)
    print(ans)