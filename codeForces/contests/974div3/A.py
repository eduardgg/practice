
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    gold = 0
    ans = 0
    for e in a:
        if e >= k:
            gold += e
        elif e == 0 and gold:
            gold -= 1
            ans += 1
    print(ans)