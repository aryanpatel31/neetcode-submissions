class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output = []
        groups = {}  # anagram.sort() -> List(str)

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in groups:
                groups[sorted_s].append(s)
            else:
                groups[sorted_s] = [s]

        for lst in groups.values():
            output.append(lst)

        return output
         
                
        
            
        
            
        
