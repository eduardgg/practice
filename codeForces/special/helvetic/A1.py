
a = input()
v = []
prefix = 0
for i in range(len(a)):
    v.append((prefix, -i, a[i]))
    if a[i] == '(':
        prefix += 1
    else:
        prefix -= 1
v.sort()
for w in v:
    print(w[2], end="")