
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    s = 0
    suma = a[0]
    if a[0] % 2 == 0:
        p += 1
    else:
        s += 1
    print(suma, end=" ")
    for k in range(1, n):
        suma += a[k]
        if a[k] % 2 == 1:
            s += 1
        res = suma - s//3
        if s%3 == 1:
            res -= 1
        print(res, end=" ")
    print()