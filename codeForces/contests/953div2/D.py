
for _ in range(int(input())):
    n, c = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a[0] += c
    maxi = 0
    for i in range(n):
        if a[i] > a[maxi]:
            maxi = i
    ans = [-1]*maxi + [0] + [j for j in range(maxi+1, n)]
    suma = 0
    for i in range(maxi):
        suma += a[i]
        ans[i] = i
        if suma < a[maxi]:
            ans[i] += 1
    print(*ans)