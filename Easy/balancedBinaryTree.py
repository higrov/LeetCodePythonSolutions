from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root == None: 
            return True
        
        def maxDepth(root: Optional[TreeNode]) -> int:
            if root == None: 
                return 0
            return 1 + max(maxDepth(root.left), maxDepth(root.right))

        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)

        if abs(left_depth - right_depth) <= 1:
            # Check if both left and right subtrees are balanced
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
    

sol = Solution()
tree = TreeNode(val = 1, left =  TreeNode(val = 3, left=None, right= None) , right= TreeNode(val= 2, left = TreeNode(val = 3, left=None, right= None), right=None)) 
print(sol.isBalanced(tree))