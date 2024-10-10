def trailingZeroes(n):
    """
    Hi haurà tants zeros com 10s a la descomposició
    Això equival al màxim nombre de 5's pel qual és divisible,
    ja que de dosos n'hi haurà "de sobres".
    """
    zeros = 0
    while n >= 5:
        n = n//5
        zeros += n
    return zeros

print (trailingZeroes(28))