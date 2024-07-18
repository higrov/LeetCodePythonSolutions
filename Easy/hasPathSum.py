from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None or targetSum<0:
            return False
        
        if root.left is None and root.right is None:
            
            if root.val == targetSum:
                return True
            
            return False
        
        return self.hasPathSum(root.left, (targetSum - root.val)) or self.hasPathSum(root.right, (targetSum-root.val))
    

tree = TreeNode(val=1, left= TreeNode(val= 2), right= TreeNode(val=3))
tree2 = TreeNode(val=5, left= TreeNode(val= 4, left= TreeNode(val = 11, left=TreeNode(val=7), right= TreeNode(val= 2))), right= TreeNode(val = 8, left = TreeNode(val = 13), right= TreeNode(val = 4, right= TreeNode(val = 1))))
sol = Solution()
print(sol.hasPathSum(tree2, 22))

#root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22