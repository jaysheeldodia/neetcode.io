from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hm = {}

        for i in strs:
            key = ''.join(sorted(strs))
            
            if key not in hm:
                hm[key] = [i]
            else:
                hm[key].append(i)

        return hm

print(Solution().groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams(strs = [""]))
print(Solution().groupAnagrams(strs = ["a"]))