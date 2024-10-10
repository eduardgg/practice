
for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    ans = 0
    for g in range(1, m+1):
        ans += min((n+g)//(g**2), n)
    print(ans)