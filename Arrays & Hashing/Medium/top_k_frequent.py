from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from heapq import heapify, heappop, heappush

        h = []

        hm = {}

        for i in nums:
            hm[i] = hm.get(i, 0) + 1

        for key, v in hm.items():
            heappush(h, (-v, key))

        final = []

        while k:
            k-=1
            temp = heappop(h)
            final.append(temp[1])
        
        return final

print(Solution().topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
print(Solution().topKFrequent(nums = [1], k = 1))
print(Solution().topKFrequent(nums = [1,2,1,2,1,2,3,1,3,2], k = 2))