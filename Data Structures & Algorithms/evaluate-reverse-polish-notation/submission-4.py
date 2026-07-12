class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) == 1:
            return int(tokens[0])

        operators = ["+", "-", "*", "/"]
        stack = []

        for token in tokens:
            if token in operators:
                operator = token
                x = stack.pop(-1)
                y = stack.pop(-1)
                res = int(eval(f"{y} {operator} {x}"))
                print(res)
                stack.append(res)
            else:
                stack.append(token)
            
        return stack[-1]
            

        
        