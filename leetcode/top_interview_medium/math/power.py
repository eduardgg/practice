def myPow(self, x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n == -1:
        return 1/x
    pot = self.myPow(x,n//2)
    pot = pot*pot
    if n % 2 == 0:
        return pot
    return pot*x