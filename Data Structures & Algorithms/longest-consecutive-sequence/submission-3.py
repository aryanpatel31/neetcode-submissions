class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if nums == []:
            return 0

        nums2 = sorted(nums)
        

        counts = []
        count = 1

        for i in range(len(nums2) - 1):
            if nums2[i] == nums2[i+1]:
                continue
            if nums2[i] + 1 == nums2[i+1]:
                count += 1
            else:
                counts.append(count)
                count = 1

        counts.append(count)
        return max(counts)

        
        

                
