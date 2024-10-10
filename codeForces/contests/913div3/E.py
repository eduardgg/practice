
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    n = int(input())
    ans = 1
    while n > 0:
        e = n % 10
        ans *= (e+2)*(e+1)//2
        n //= 10
    print(ans)