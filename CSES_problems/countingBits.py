
n = int(input())
ans = 0
incr = 1
div = 1
while incr:
    incr = div * ((n+1)//(2*div)) + max(0, (n+1)%(2*div)-div)
    ans += incr
    div *= 2
print(ans)