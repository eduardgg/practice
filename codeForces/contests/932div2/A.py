
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    s = input()
    ok = True
    for i in range(len(s)//2):
        if s[i] < s[-1-i]:
            print(s)
            ok = False
            break
        elif s[i] > s[-1-i]:
            print(s[::-1] + s)
            ok = False
            break
    if ok:
        print(s)