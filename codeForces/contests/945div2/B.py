
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    totor = 0
    for e in a:
        totor |= e
    maxcons = 0
    for k in range(20):
        if totor & (1 << k):
            cons = 0
            for e in a:
                if not e & (1 << k):
                    cons += 1
                    if cons > maxcons:
                        maxcons = cons
                else:
                    cons = 0
    print(maxcons+1)