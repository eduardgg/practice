
for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    a = input()
    b = input()
    l = 0
    for e in b:
        if e == a[l]:
            l += 1
            if l == n:
                break
    print(l)