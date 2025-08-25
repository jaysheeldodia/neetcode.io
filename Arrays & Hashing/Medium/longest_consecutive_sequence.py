from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()

        cont = 1
        max_cont = 1
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                cont += 1 
            else:
                max_cont = max(max_cont, cont)
                cont = 1

        max_cont = max(max_cont, cont)

        return max_cont

print(Solution().longestConsecutive(nums = [100,4,200,1,3,2]))
print(Solution().longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))
print(Solution().longestConsecutive(nums = [1, 0, 1, 2]))