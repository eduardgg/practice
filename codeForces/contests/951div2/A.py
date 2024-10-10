
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    minim = 10**10
    for i in range(n-1):
        minim = min(minim, max(a[i],a[i+1]))
    ans = minim - 1
    print(ans)