from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        num_dict = dict()

        for num in nums:
            if num in num_dict.keys():
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        
        return max(num_dict, key=num_dict.get)
    
    def majorityElement_alt(self,nums:List[int]) -> int :
        nums.sort()
        n = len(nums)

        return nums[n // 2]
sol = Solution()

print(sol.majorityElement_alt([2,2,1,1,1,2,2]))