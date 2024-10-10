line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    a, b, c = line()
    ans = a + b//3
    b %= 3
    if b>0 and b+c < 3:
        print(-1)
    else:
        ans += (b+c)//3
        if (b+c)%3 != 0:
            ans += 1
        print(ans)