from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        while k != len(nums):
            if nums[k] == val:
                nums.remove(val)
            else:
                k += 1

        return k , nums
    

sol = Solution()
nums = [0,1,2,2,3,0,4,2,2]
val = 2
print(sol.removeElement(nums,val))