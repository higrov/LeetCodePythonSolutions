from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None : 
            return 0
        
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        if root.left is None and root.right is None: 
            return 1 
        
        elif root.left is None:
            return 1 + right_depth
        
        elif root.right is None:
            return 1 + left_depth
        
        return 1 + min(left_depth, right_depth)


tree = TreeNode(val = 2, left = None, right=TreeNode(val = 3, left= None, right= TreeNode(val = 4, left = None, right= TreeNode(val = 5, right= TreeNode(val = 6)))))

tree2 = TreeNode(val=3, left= TreeNode(val= 9), right= TreeNode(val = 20, left = TreeNode(val = 15), right= TreeNode(val = 7)))
sol = Solution()
print(sol.minDepth(tree))