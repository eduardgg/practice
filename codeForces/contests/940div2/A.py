
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    a.sort()
    ans = 0
    count = 1
    for i in range(1, n):
        if a[i] == a[i-1]:
            count += 1
            if count == 3:
                count = 0
                ans += 1
        else:
            count = 1
    print(ans)