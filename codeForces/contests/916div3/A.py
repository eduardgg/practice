
for _ in range(int(input())):
    n = int(input())
    s = input()
    q = [0]*26
    for e in s:
        q[ord(e)-65] += 1
    ans = 0
    for i in range(26):
        if q[i] > i:
            ans += 1
    print(ans)