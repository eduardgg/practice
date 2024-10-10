
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    s = input()
    uns = 0
    for c in s:
        if c == '1':
            uns += 1

    ans = -1
    if uns >= n-uns:
        ans = 0
    cur = 0
    pos = set()
    for i in range(n):
        if s[i] == '1':
            cur += 1
        if i+1-cur >= cur and uns-cur >= n-(i+1)-(uns-cur):
            if abs(n/2 - (i+1)) < abs(n/2 - ans):
                ans = i+1
                if ans >= n//2:
                    break
    
    print(ans)