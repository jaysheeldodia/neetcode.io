from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        
        for i in range(len(nums)):
            num = nums[i]

            x = target - num
            
            if hm.get(num, -1) == -1:
                hm[x] = i
            else:
                return [hm[num], i]
            

print(Solution().twoSum(nums = [2,7,11,15], target = 9))
print(Solution().twoSum(nums = [3, 2, 4], target = 6))
print(Solution().twoSum(nums = [3, 3], target = 6))