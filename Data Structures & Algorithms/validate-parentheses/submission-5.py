class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return False
        if len(s) %2 != 0:
            return False

        opens = {
                "(" : 0,
                "{" : 1,
                "[" : 2
                }
        
        closers = {
                ")" : 0,
                "}" : 1,
                "]" : 2
                }

        

        my_stack = []
        for char in s:
            if char in opens:
                my_stack.append(char)
            elif char in closers:
                if not my_stack:
                    return False
                if opens[my_stack[-1]] != closers[char]:
                    return False
                else:
                    my_stack.pop()

        if len(my_stack) == 0:
            return True
        else:
            return False
