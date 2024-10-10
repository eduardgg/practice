
def binaryToNum(binary):
    num = 0
    for i in range(len(binary)):
        num = 2*num + int(binary[i])
    return num

def numToBinary(num):
    string = ""
    while num != 0:
        string += str(num % 2)
        num = num // 2
    return string[::-1]

def extend(string, n):
    return "0"*(max(n-len(string), 0)) + string

def XOR(s1, s2):
    if len(s1) > len(s2):
        s2 = "0"*(len(s1)-len(s2)) + s2
    else:
        s1 = "0"*(len(s2)-len(s1)) + s1
    s = ""
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            s += '0'
        else:
            s += '1'
    return s

def OR(s1, s2):
    if len(s1) > len(s2):
        s2 = "0"*(len(s1)-len(s2)) + s2
    else:
        s1 = "0"*(len(s2)-len(s1)) + s1
    s = ""
    for i in range(len(s1)):
        if s1[i] == '1' or s2[i] == '1':
            s += '1'
        else:
            s += '0'
    return s

def AND(s1, s2):
    if len(s1) > len(s2):
        s2 = "0"*(len(s1)-len(s2)) + s2
    else:
        s1 = "0"*(len(s2)-len(s1)) + s1
    s = ""
    for i in range(len(s1)):
        if s1[i] == '0' or s2[i] == '0':
            s += '0'
        else:
            s += '1'
    return s


t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    xor = "0"
    for ai in a:
        xor = XOR(xor, numToBinary(ai))

    if n % 2 == 0:
        maxXor = xor
        minXor = ""
        puntsMax = 0
        for bi in b:
            punts = 0
            bibin = numToBinary(bi)
            xor = extend(xor, len(bibin))
            for i in range(len(bibin)):
                if bibin[-1-i] == '1' and xor[-1-i] == '1':
                    punts += 1
            if punts > puntsMax:
                puntsMax = punts
                bimillor = bibin
        bimillor = extend(bimillor, len(xor))
        for i in range(len(xor)):
            if bimillor[i] == '1':
                minXor += '0'
            else:
                minXor += xor[i]

    else:
        maxXor = ""
        minXor = xor
        puntsMax = 0
        for bi in b:
            punts = 0
            bibin = numToBinary(bi)
            xor = extend(xor, len(bibin))
            for i in range(len(bibin)):
                if bibin[-1-i] == '1' and xor[-1-i] == '0':
                    punts += 1
            if punts > puntsMax:
                puntsMax = punts
                bimillor = bibin
        bimillor = extend(bimillor, len(xor))
        for i in range(len(xor)):
            if bimillor[i] == '1':
                maxXor += '1'
            else:
                maxXor += xor[i]


    print(binaryToNum(minXor), binaryToNum(maxXor))