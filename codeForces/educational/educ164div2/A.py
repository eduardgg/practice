
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    n, m, k = line()
    if n - (n//m + (n%m != 0)) > k:
        print("YES")
    else:
        print("NO")