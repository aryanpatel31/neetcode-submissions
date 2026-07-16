class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        
        storage = []
        for i in range(len(position)):
            storage.append((position[i], speed[i]))
        
        storage.sort(key = lambda x: x[0], reverse = True)
  

        times = [ (target - x[0])/ x[1] for x in storage]
        
        stack = []
        
        for time in times:
            if stack == []:
                stack.append(time)
            elif time <= stack[-1]:
                continue
            else:
                stack.append(time)
        
        return len(stack)