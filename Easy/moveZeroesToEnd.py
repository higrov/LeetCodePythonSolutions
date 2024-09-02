from typing import List
class Solution:
    def moveZeroes_vishnu(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l, r = 0, 0
        while r<n:
            nums[l] = nums[r]
            if nums[l]!=0:
                l+=1
            r+=1
        while l<n:
            nums[l]=0
            l+=1


    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = 0 
        for i in nums:
            if i == 0:
                n+=1

        if n != len(nums):
            i = 0
            j = 0
            
            while j < len(nums):
                if nums[j] != 0:
                    nums[i] = nums[j]
                    i+=1
                
                j+=1
            
            if j == len(nums):
                while i < j: 
                    nums[i] = 0
                    i += 1            
            
            

