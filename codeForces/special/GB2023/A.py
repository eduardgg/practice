t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    prod = 1
    for i in a:
        prod *= i
    if 2023%prod != 0:
        print("NO")
    else:
        print("YES")
        print(2023//prod, end=" ")
        for j in range(k-1):
            print(1, end=" ")
        print()
    
