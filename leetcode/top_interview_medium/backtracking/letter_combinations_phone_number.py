def letterCombinations(digits):
    letters = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
    }
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return letters[digits[0]]
    return [i+j for i in letterCombinations(digits[0]) for j in letterCombinations(digits[1:])]

digits = "23"
print(letterCombinations(digits))
digits = ""
print(letterCombinations(digits))
digits = "2"
print(letterCombinations(digits))