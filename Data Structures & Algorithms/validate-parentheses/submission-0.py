class Solution:
    def isValid(self, s: str) -> bool:
        validParentheses = {'(': ')', '{':'}', '[':']'}
        parentheses = []

        for i in s:
            if len(parentheses) == 0:
                if i in validParentheses:
                    parentheses.append(i)
                    continue
                else:
                    return False

            if i in validParentheses:
                parentheses.append(i)

            if len(parentheses) > 0 and i not in validParentheses:
                temp = parentheses.pop()
                if validParentheses[temp] != i:
                    return False

        if len(parentheses) == 0:
            return True
        else:
            return False