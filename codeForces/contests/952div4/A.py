
for _ in range(int(input())):
    a, b = input().split()
    a, b = b[0] + a[1:], a[0] + b[1:]
    print(a, b)