
for _ in range(int(input())):
    n = int(input())
    ans = []
    for a in range(1, 10**4+1):
        l = len(str(n))
        for b in range (max(1, l*a-7), l*a):
            num = str(n*a-b)
            if len(num) != l*a-b:
                continue
            if num == (str(n)*7)[:len(num)]:
                ans.append((a, b))
    print(len(ans))
    for (a, b) in ans:
        print(a, b)