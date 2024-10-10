
for _ in range(int(input())):
    n = int(input())
    s = input()
    abc = set()
    ans = 0
    for i in range(n):
        abc.add(s[i])
        ans += len(abc)
    print(ans)