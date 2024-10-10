
for _ in range(int(input())):
    n = int(input())
    x, y = [], []
    for _ in range(n):
        xi, yi = list(map(int, input().split()))
        x.append(xi)
        y.append(yi)
    xs, ys, xt, yt = list(map(int, input().split()))
    d = (xs - xt)**2 + (ys - yt)**2
    if any([d >= (xt - x[i])**2 + (yt - y[i])**2 for i in range(n)]):
        print("NO")
    else:
        print("YES")