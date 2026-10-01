class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for i in tokens:
            match i:
                case '+':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a + b)
                case '-':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a - b)  
                case '*':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a * b)
                case '/':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(a / b))  
                case _:
                    stack.append(int(i))

        return stack[0]