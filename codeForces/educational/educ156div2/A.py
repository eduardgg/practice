t = int(input())
for _ in range(t):
    n = int(input())
    if n <= 6 or n == 9:
        print("NO")
    elif n%3 == 0:
        print("YES")
        print("1 4", n-5)
    else:
        print("YES")
        print("1 2", n-3)