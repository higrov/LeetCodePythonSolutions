from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root == None: 
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        

    

sol = Solution()
tree = TreeNode(val = 1, left = None , right= TreeNode(val= 2, left = TreeNode(val = 3, left=None, right= None), right=None)) 
print(sol.maxDepth(tree))
