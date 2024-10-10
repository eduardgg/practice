
def f(i, j, o, cami):
    if linies[i][j] == "X":
        o += 1
    if o > k:
        return
    if (i+1 == n) and (j+1 == m) and (o == k):
        print(cami)
        return
    if i+1 < n:
        f(i+1, j, o, cami + "D")
    if j+1 < m:
        f(i, j+1, o, cami + "R")

while True:
    linia = input().split(" ")
    n, m, k = (int(linia[0]), int(linia[1]), int(linia[2]))
    linies = []
    for i in range(n):
        linies += [input()]
    cami = ""
    f(0, 0, 0, cami)
    print("----------")
    enter = input()
    