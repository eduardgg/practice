
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()
    a.pop()
    ans = 0
    for e in a:
        ans += 2*e - 1
    print(ans)