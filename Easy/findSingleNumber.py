from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        occur = dict()

        for num in nums:
            occur[num] = nums.count(num)

        res = next(key for key in occur.keys() if occur[key] == 1)

        return res
    

sol = Solution()

num_list = [4,1,2,1,2]

print(sol.singleNumber(num_list))