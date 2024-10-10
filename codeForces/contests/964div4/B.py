
for _ in range(int(input())):
    a1, a2, b1, b2 = list(map(int, input().split()))
    ans = 0
    if a1 > b1 and a2 >= b2:
        ans += 1
    elif a1 == b1 and a2 > b2:
        ans += 1
    if a2 > b1 and a1 >= b2:
        ans += 1
    elif a2 == b1 and a1 > b2:
        ans += 1
    print(2*ans)