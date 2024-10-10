
for _ in range(int(input())):
    n = int(input())
    f1 = input()
    f2 = input()
    ans = 0
    for i in range(1, n-1):
        if f1[i-1:i+2] == '...' and f2[i-1:i+2] == 'x.x':
            ans += 1
        if f2[i-1:i+2] == '...' and f1[i-1:i+2] == 'x.x':
            ans += 1
    print(ans)