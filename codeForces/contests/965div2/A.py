
for _ in range(int(input())):
    xc, yc, k = list(map(int, input().split()))
    if k%2:
        print(xc, yc)
    for i in range(k//2):
        print(xc+1+i, yc)
        print(xc-1-i, yc)