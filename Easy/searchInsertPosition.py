from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        
        while left < right:
            mid = (left + right) // 2 

            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        return left
    


sol = Solution()
nums = [1,3,5,6]
target = 4

print(sol.searchInsert(nums,target))