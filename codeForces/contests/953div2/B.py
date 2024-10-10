
for _ in range(int(input())):
    n, a, b = list(map(int, input().split()))
    if b <= a:
        print(a*n)
    elif b-a < n:
        ans = (b*(b+1) - a*(a+1)) // 2 + a*(n-(b-a))
        print(ans)
    else:
        ans = (b*(b+1) - (b-n)*(b-n+1)) // 2
        print(ans)