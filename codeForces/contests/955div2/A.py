
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    c, d = list(map(int, input().split()))
    print("YES" if (b-a)*(d-c) > 0 else "NO")