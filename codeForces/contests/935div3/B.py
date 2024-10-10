
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    a, b, m = line()
    ans = m//a+1 + m//b + 1
    print(ans)