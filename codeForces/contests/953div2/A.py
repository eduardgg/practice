
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = a.pop()
    ans += max(a)
    print(ans)