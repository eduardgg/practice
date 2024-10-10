
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] == a[-1]:
        print("NO")
    else:
        print("YES")
        print("RB" + "R"*(n-2))