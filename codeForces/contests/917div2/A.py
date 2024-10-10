
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    zeros = 0
    negs = 0
    for e in a:
        negs += (e < 0)
        zeros += (e == 0)
    if negs%2 or zeros:
        print(0)
    else:
        print(1)
        print(1, 0)