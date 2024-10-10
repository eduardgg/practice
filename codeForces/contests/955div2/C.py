
t = int(input())
for tc in range(t):
    n, l, r = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ans = 0
    suma = 0
    i = 0
    for j in range(n):
        suma += a[j]
        while suma > r:
            suma -= a[i]
            i += 1
        if l <= suma:
            suma = 0
            ans += 1
            i = j+1
    print(ans)