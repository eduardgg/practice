
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range((n-1)//2):
        ans += min((a[i] == a[i+1]) + (a[-1-i] == a[-1-i-1]), (a[i] == a[-1-i-1]) + (a[-1-i] == a[i+1]))
    if n%2 == 0:
        ans += (a[n//2] == a[n//2 - 1])
    print(ans)