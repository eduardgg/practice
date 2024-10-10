
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    n = int(input())
    s = set(line())
    maxim = max(s)
    if 1 in s:
        count = 1
        for e in range(2, maxim+1):
            if e not in s:
                break
            count += 1
        if (count % 2 and maxim != count) or (not count % 2 and maxim == count):
            print("Bob")
            continue
    print("Alice")