class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = []
        for i, temp in enumerate(temperatures):

            if i == len(temperatures) - 1:
                res.append(0)
                break

            stack = []
            index = i

            while (index + 1) < len(temperatures) and temperatures[index+1] <= temp:

                stack.append(temperatures[index+1])
                index += 1
            
            if index == len(temperatures) - 1:
                res.append(0)
            else:
                res.append(len(stack) + 1)
        
        return res
