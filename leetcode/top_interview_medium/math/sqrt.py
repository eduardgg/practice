def mySqrt(x):
    if x <= 1:
        return x
    low = 1
    high = x
    while (low < high - 1):
        mid = (low+high) // 2
        square = mid*mid
        if square <= x:
            low = mid
        else:
            high = mid
    return low

print(mySqrt(0))
print(mySqrt(1))
print(mySqrt(3))
print(mySqrt(6))
print(mySqrt(8))
print(mySqrt(9))
print(mySqrt(120))
print(mySqrt(125))
print(mySqrt(144))