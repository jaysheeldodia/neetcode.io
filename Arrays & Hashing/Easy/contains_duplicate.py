from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for i in nums:
            x = hm.get(i, 0)
            if x:
                return True
            else:
                hm[i] = 1

        return False