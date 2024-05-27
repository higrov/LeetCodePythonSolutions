from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1: 
            nums1= nums2[:n]
        
        elif not nums2:
            nums1 = nums1[:m]
        
        else:
            def searchInsert(nums: List[int], m : int, target: int) -> int:
                left, right = 0, m

                while left < right:
                    mid = (left + right) // 2 

                    if nums[mid] >= target:
                        right = mid
                    else:
                        left = mid + 1

                return left

            for num in nums2:
                pos = searchInsert(nums1,m,num)
                nums1.insert(pos,num)
                m +=1
            
            nums1 = nums1[:m]
            print(nums1)


sol = Solution()
nums1 = [0]
m = 0
n = 1
nums2 = [1]

sol.merge(nums1,m,nums2,n)