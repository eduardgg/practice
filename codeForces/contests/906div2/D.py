t = int(input())
for _ in range(t):
    n, c = list(map(int, input().split()))
    a = list(map(int, input().split()))
    v = [(a[i]-(i+1)*c, i+1) for i in range(1, n)]
    v.sort()
    sum = a[0]
    ok = True
    while v:
        k, node = v.pop()
        if sum + k >= 0:
            sum += k + node*c
        else:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")