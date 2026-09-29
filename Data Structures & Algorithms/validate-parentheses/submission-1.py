class Solution:
    def isValid(self, s: str) -> bool:

        validParentheses = {'(': ')', '{':'}', '[':']'}
        parentheses = []


        if len(s)%2!=0:
            return False

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

        return len(parentheses) == 0
            
        