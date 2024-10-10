
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    if n == 1:
        if k == 0:
            print("YES")
            print(1)
        else:
            print("NO")
    elif n == 2:
        if k == 0:
            print("YES")
            print(1, 2)
        elif k == 2:
            print("YES")
            print(2, 1)
        else:
            print("NO")
    elif k % 2 or k > 2*(n//2)*((n+1)//2):
        print("NO")
    else:
        print("YES")
        a = [i+1 for i in range(n)]
        for i in range((n-1)//2 - 1):
            if 2*(a[-1-i] - a[i]) <= k:
                k -= 2*(a[-1-i] - a[i])
                a[-1-i], a[i] = a[i], a[-1-i]
        pos = (n-3)//2
        if pos >= 0 and k > 0:
            if k == 8:
                a[pos], a[pos+1], a[pos+2], a[pos+3] = a[pos+3], a[pos+2], a[pos+1], a[pos]
            elif k == 6:
                a[pos], a[pos+3] = a[pos+3], a[pos]
            elif k == 4:
                a[pos], a[pos+2] = a[pos+2], a[pos]
            else:
                a[pos], a[pos+1] = a[pos+1], a[pos]
        print(*a)