def titleToNumber(columnTitle):
    number = 0
    mult = 1
    for i in range(len(columnTitle)):
        number += mult * (ord(columnTitle[len(columnTitle)-1-i])-ord('A')+1)
        mult *= 26
    return number

print (titleToNumber("A"))
print (titleToNumber("AB"))
print (titleToNumber("ZY"))
print (titleToNumber("FXSHRXW"))