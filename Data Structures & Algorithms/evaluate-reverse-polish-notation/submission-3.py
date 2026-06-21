class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+","-","*","/"}
        stack = []
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            elif i == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b) 
            elif i == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif i == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b) 
            elif i == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))         
        return stack[0]  
