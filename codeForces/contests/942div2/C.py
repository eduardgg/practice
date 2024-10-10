
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, k = line()
    a = line()
    a.sort()
    suma = 0
    ok = False
    for i in range(n):
        suma += a[i]
        if (i+1)*a[i] - suma > k:
            ok = True
            q = k + suma - a[i]
            ans = (q//i)*n - (n-1) + q%i + n-i
            break
    if not ok:
        k -= ((i+1)*a[i] - suma)
        ans = (a[-1] + k//n)*n - (n-1) + k%n

    print(ans)