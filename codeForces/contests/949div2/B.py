
for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    ans = 0
    for i in range((n+m).bit_length()):
        if (n+m) & (1 << i) or (n >= m and ((n-m) & (1 << i))) or (2*m+1) > (1 << i):
            ans += (1 << i)
    print(ans)