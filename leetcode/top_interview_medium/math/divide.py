def divide(dividend, divisor):
    if divisor == 1:
        return dividend
    if dividend == 0:
        return 0
    if dividend < 0:
        if divisor < 0:
            return divide(-dividend, -divisor)
        return - divide(-dividend, divisor)
    if divisor < 0:
        return - divide(dividend, -divisor)
    if dividend < divisor:
        return 0
    double = divisor + divisor
    if dividend < double:
        return 1
    quotient = divide(dividend, double)
    residue = 0
    if dividend - quotient * double > divisor:
        residue += 1
    return 2 * quotient + residue

print(divide(21,4))