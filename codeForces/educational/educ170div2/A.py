
for _ in range(int(input())):
    a = input()
    b = input()
    count = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            count += 1
        else:
            break
    print(len(a) + len(b) - max(0, count - 1))