
for _ in range(int(input())):
    n, x = list(map(int, input().split()))
    ans = 0
    for a in range(1, x-1):
        for b in range(1, min((n-a)//(a+1) + 1, x-a)):
            ans += min(x-a-b, (n-a*b)//(a+b))
    print(ans)