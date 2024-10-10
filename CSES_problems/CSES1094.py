
n = int(input())
a = list(map(int, input().split()))
cur = 0
ans = 0
for e in a:
    if e >= cur:
        cur = e
    else:
        ans += cur-e
print(ans)