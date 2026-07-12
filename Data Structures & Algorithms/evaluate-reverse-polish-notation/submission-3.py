class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) == 1:
            return int(tokens[0])

        operators = ["+", "-", "*", "/"]
        stack = []

        while tokens:
            if tokens[0] in operators:
                operator = tokens.pop(0)
                x = stack.pop(-1)
                y = stack.pop(-1)
                res = int(eval(f"{y} {operator} {x}"))
                print(res)
                stack.append(res)
            else:
                stack.append(tokens.pop(0))
            
        return stack[-1]
            

        
        