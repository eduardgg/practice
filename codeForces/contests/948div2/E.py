
t = int(input())
for _ in range(t):
    n = int(input())
    c = [0]
    for i in range(1, n):
        print("?", i, i+1)
        res = input()
        c.append(c[-1] if res == "YES" else 1-c[-1])
    print("!", *c)