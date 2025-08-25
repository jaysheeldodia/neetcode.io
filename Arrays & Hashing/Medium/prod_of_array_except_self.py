from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zero = nums.count(0)

        if count_zero > 1:
            return [0] * len(nums)

        p = 1 

        for i in nums:
            if i != 0:
                p*=i

        final = []
        if count_zero != 1:
            for i in nums:
                final.append(p//i)
        else:
            for i in nums:
                if i == 0:
                    final.append(p)
                else:
                    final.append(0)
        return final

print(Solution().productExceptSelf(nums=[1, 2, 3, 4]))
print(Solution().productExceptSelf(nums = [-1,1,0,-3,3]))