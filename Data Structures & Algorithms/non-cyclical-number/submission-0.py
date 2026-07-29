class Solution:
    def isHappy(self, n: int) -> bool:
        
        nums = []
        for digit in str(n):
            nums.append(digit)
        
        visited = []

        num = int(''.join(nums))
        
        while num not in visited:
            visited.append(num)
            total = 0
            for dig in nums:
                total += (int(dig) * int(dig))
            num = total

            if total == 1:
                return True

            nums = []
            for digit in str(num):
                nums.append(digit)
        
        return False
                
            
        
        