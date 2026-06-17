class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        low = 0
        high = len(numbers) - 1

        res = numbers[low] + numbers[high]

        while res != target:
            if res < target:
                low += 1
                res = numbers[low] + numbers[high]
            elif res > target:
                high -= 1
                res = numbers[low] + numbers[high]

        return [low+1, high + 1]

            
    



