
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    ans = []
    for _ in range(q):
        l, k = list(map(int, input().split()))
        i = l-1
        prod = a[i]
        if a[i] < k:
            ans += [-1]
            continue
        while prod >= k:
            i += 1
            if i == len(a):
                break
            prod &= a[i]
        ans += [i]
    for a in ans:
        print(a, end = " ")
    print()