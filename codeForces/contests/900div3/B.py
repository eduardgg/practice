
t = int(input())
for _ in range(t):
    n = int(input())
    print("1", end=" ")
    for i in range(n-2):
        print(2*i+3, end=" ")
    print(2*n-1)