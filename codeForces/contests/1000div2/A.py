
for _ in range(int(input())):
    l, r = list(map(int, input().split()))
    print(r - l + (l == r == 1))