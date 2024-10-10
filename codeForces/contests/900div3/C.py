
t = int(input())
for _ in range(t):
    n, k, x = list(map(int, input().split()))
    if x < k*(k+1)//2 or x > n*(n+1)//2 - (n-k)*(n-k+1)//2:
        print("NO")
    else:
        print("YES")
