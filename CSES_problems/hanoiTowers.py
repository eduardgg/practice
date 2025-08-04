
# i, j different stacks among 1, 2, 3
# The auxiliary stack will be k = 6-i-j

def f(n, i, j):
    if n == 1:
        print(i, j)
        return
    k = 6-i-j
    f(n-1, i, k)
    print(i, j)
    f(n-1, k, j)

n = int(input())
print(2**n-1)
f(n, 1, 3)