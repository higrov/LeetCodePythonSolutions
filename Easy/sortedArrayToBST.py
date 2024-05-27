from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode({self.val}, left = {self.left.__repr__()}, right = {self.right.__repr__()})"

class Solution:
    def sortedArrayToBST(self, nums: List[int])-> Optional[TreeNode]:

        if not nums:
            return None
        
        mid = len(nums) // 2

        return TreeNode(val = nums[mid], left= self.sortedArrayToBST(nums[:mid]), right= self.sortedArrayToBST(nums[mid+1:]))
    
sol =Solution()
nums = [-10,-3,0,5,9]

print(sol.sortedArrayToBST(nums))