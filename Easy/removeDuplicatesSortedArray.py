from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicates = 0
        i =0 
        while i+1 < len(nums):
            temp = nums[i]
            temp2 = nums[i+1]

            while temp == temp2:
                nums.remove(temp2)
                duplicates += 1
                if i+1 >= len(nums):
                    break
                temp2 = nums[i+1]
            i +=1

        return len(nums) , nums



sol = Solution()
list2 = [1,1]

print(sol.removeDuplicates(list2))