class Solution(object):
    def generateParentheses(n):
        def f(m=n, v=['']*2*n, o=0, t=0):
            # o són els parèntesis oberts
            # t són els parèntesis tancats
            # n és el nombre dels parells de parèntesis
            # v és la string de parèntesis
            if t == m:
                mystring = ""
                for x in v:
                    mystring += x
                answer.append(mystring)
                return
            if o < m:            
                v[o+t] = '('
                f(m, v, o+1, t)
            if o > t:
                v[o+t] = ')'
                f(m, v, o, t+1)
            return

        answer = []
        f()
        return answer
    
    print(generateParentheses(4))