def longestPalindrome(s):
    if len(s) == 0:
        return s
        
    # Palíndroms amb 1 lletra central
    max_mig_1 = 0
    max_sidelength_1 = 0
    for i in range(len(s)):
        sidelength = 0
        mig = i
        for j in range(min(mig,len(s)-1-mig)):
            if s[mig-(j+1)] != s[mig+(j+1)]:
                break
            sidelength += 1
        if sidelength > max_sidelength_1:
            max_sidelength_1 = sidelength
            max_mig_1 = mig

    # Palíndroms amb 2 lletres centrals
    # Les lletres centrals ara són max_mig i max_mig + 1
    max_mig_2 = 0
    max_sidelength_2 = 0
    trobat = False
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            continue
        trobat = True
        sidelength = 0
        mig = i
        for j in range(min(mig,len(s)-2-mig)):
            if s[mig-(j+1)] != s[(mig+1)+(j+1)]:
                break
            sidelength += 1
        if sidelength >= max_sidelength_2:
            max_sidelength_2 = sidelength
            max_mig_2 = mig

    if (trobat and (1 + 2*max_sidelength_1 < 2 + 2*max_sidelength_2)):
        return s[max_mig_2 - max_sidelength_2 : (max_mig_2 + 1) + max_sidelength_2 + 1]
    return s[max_mig_1 - max_sidelength_1 : max_mig_1 + max_sidelength_1 + 1]


print(longestPalindrome("asddscsw"))
print(longestPalindrome("VV"))
print(longestPalindrome("VAVAVA"))
print(longestPalindrome("babad"))
print(longestPalindrome("asdcbbd"))