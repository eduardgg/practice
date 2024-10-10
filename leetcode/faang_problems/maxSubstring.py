# Given a string s, what is the length of the
# longest substring without repeating characters?

# Mètode 1:
# És el més intuïtiu, i té un "worst case cost"
# de O(m·n) en temps i O(1) en espai, on:
#   n: longitud de la paraula s
#   m: tamany de l'alfabet
def maxSubstring1(s):
    maxlen = 0
    prevlen = 1
    for i in range(len(s)-1):
        leng = 1
        for j in range(prevlen):
            if s[i-j] == s[i+1]:
                break
            leng += 1
        maxlen = max(maxlen, leng)
        prevlen = leng
    return maxlen

# Mètode 2:
# Fent servir un diccionari, ocupant espai O(m), millorem
# el cost temporal a O(n), a base de recordar l'última 
# aparició de cada lletra de l'alfabet.
def maxSubstring2(s):
    dict = {}
    leng = 0
    maxlen = 0
    for i in range(len(s)):
        if s[i] not in dict.keys() or dict[s[i]] < i - leng:
            leng = leng + 1
        else:
            leng = i - dict[s[i]]
        dict[s[i]] = i
        maxlen = max(maxlen, leng)
    return maxlen

s = "abcabcbb"
r = "abcdeafbdgcbb"
print(maxSubstring1(r))
print(maxSubstring2(r))