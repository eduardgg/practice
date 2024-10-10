
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, k = line()
    if k > n:
        print("NO")
    elif k == n:
        print("YES")
        print(1)
        print(1)
    elif k <= (n+1)//2:
        print("YES")
        print(2)
        print(n-k+1, 1)
    elif k == 1:
        print("YES")
        print(1)
        print(n)
    else:
        print("NO")