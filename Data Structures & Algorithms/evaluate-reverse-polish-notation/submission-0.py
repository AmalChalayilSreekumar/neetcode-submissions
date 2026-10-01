class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for i in tokens:
            if i in {'+', '-', '*', '/'}:
                tempNum = stack.pop()
                tempNum1 = stack.pop()

                match i:
                    case '+':
                        stack.append(tempNum1+tempNum)
                    case '-':
                        stack.append(tempNum1-tempNum)
                    case '*':
                        stack.append(tempNum1*tempNum)
                    case '/':
                        stack.append(int(tempNum1/tempNum))
            else:
                stack.append(int(i))

        return stack[0]