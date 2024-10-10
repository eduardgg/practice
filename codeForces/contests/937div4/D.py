
line = lambda : list(map(int, input().split()))

s = set()
for i in range(2, 100001):
    bin, j = True, i
    while j > 0:
        if j%10 > 1:
            bin = False
            break
        j //= 10
    if bin:
        s.add(i)
    else:
        for e in s:
            if i%e == 0 and i//e in s:
                s.add(i)
                break
s.add(1)

for _ in range(int(input())):
    n = int(input())
    if n in s:
        print("YES")
    else:
        print("NO")