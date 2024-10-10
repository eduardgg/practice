
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    diags = -1
    k += n
    for i in range(n, 0, -1):
        if k > 0:
            k -= i
            diags += 1
        else:
            break
        if k > 0:
            k -= i
            diags += 1
        else:
            break
    print(diags)