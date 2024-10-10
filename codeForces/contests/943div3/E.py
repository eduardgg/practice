
for _ in range(int(input())):
    n = int(input())
    print(1, 1)
    print(2, 1)
    p = 2
    if n > p:
        print(n, n)
        p += 1
    if n == 3:
        print()
        continue
    for i in range(3, n+1, 2):
        print(1, i)
        p += 1
    i = 1
    while p < n:
        print(n-i, n)
        i += 1
        p += 1
    print()