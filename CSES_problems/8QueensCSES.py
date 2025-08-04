
col = [False]*8
diag1 = [False]*15
diag2 = [False]*15
occu = []
for _ in range(8):
    s = input()
    occu.append([True if s[i] == '*' else False for i in range(8)])

ans = [0]

def f(i):
    if i == 8:
        ans[0] += 1
        return
    for j in range(8):
        if not col[j] and not diag1[j+i] and not diag2[j-i+7] and not occu[i][j]:
            col[j] = diag1[j+i] = diag2[j-i+7] = True
            f(i+1)
            col[j] = diag1[j+i] = diag2[j-i+7] = False

f(0)
print(ans[0])