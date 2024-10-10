class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        strings = set()
        
        def r(s, f, p, fo, ft, i, O, T):
            # s: paraula inicial a arreglar
            # f: paraula que estem construïnt
            # p: posició de s a analitzar si eliminar
            # fo: nombre de "(" que té f actualment
            # ft: nombre de ")" que té f actualment
            # i: nombre de "(" (o ")") que ha de tenir f
            # O: nombre de "(" que queden a s a partir de p
            # T: nombre de ")" que queden a s a partir de p

            # Casos Especials:
            # 1 - La paraula és vàlida, per construcció
            if p == len(s):
                if fo == ft == i:
                    strings.add(f)
                return
            # 2 - No ens queden prou parèntesis per acabar
            if i-fo > O or i-ft > T:
                return
            # 3 - Ens hem passat de parèntesis
            if fo > i or ft > i:
                return
            
            if s[p] == "(":
                r(s, f, p + 1, fo, ft, i, O - 1, T)
                r(s, f + "(", p + 1, fo + 1, ft, i, O - 1, T)
            elif s[p] == ")":
                r(s, f, p + 1, fo, ft, i, O, T - 1)
                if fo > ft:
                    r(s, f + ")", p + 1, fo, ft + 1, i, O, T - 1)
            else:
                r(s, f + s[p], p + 1, fo, ft, i, O, T)
            return
        
        O, T = 0, 0
        for char in s:
            if char == ")":
                T += 1
            elif char == "(":
                O += 1
        i = min(O, T)
        while i >= 0:
            r(s, "", 0, 0, 0, i, O, T)
            if len(strings) > 0:
                output = []
                for str in strings:
                    output += [str]
                return output
            i -= 1
    

sol = Solution()
print(sol.removeInvalidParentheses("()())()"))
print(sol.removeInvalidParentheses("(a)())()"))
print(sol.removeInvalidParentheses("((((((((((((((((((((aaaaa"))