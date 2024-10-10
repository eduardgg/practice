
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    maxim = max(a)
    for i in range(n):
        a[i] %= 2*k
    a.sort()

    mom = -1
    for i in range(n-1):
        if a[i+1]-a[i] > k:
            mom = a[i]
            break
    if mom == -1 and a[-1] - a[0] < k:
        mom = a[-1]
    
    if mom == -1:
        print(-1)
    else:
        ans = maxim + ((mom - maxim) % k)
        print(ans)