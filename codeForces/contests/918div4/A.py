
t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    for i in range(3):
        if a[i] == a[(i+1)%3]:
            print(a[(i+2)%3])