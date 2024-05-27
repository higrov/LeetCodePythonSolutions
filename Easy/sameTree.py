from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p is None and q is None: 
            return True
        
        elif p is None and q is not None or q is None and p is not None: 
            return False
        else: 
            return (p.val == q.val ) and self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)


tree = TreeNode(val = 1, left = None , right= TreeNode(val= 2, left = TreeNode(val = 3, left=None, right= None), right=None))
tree2 = TreeNode(val = 1, left = TreeNode(val= 4, left = TreeNode(val = 5, left=None, right= None), right=TreeNode(val = 6, left = None,right=None)) , right= TreeNode(val= 2, left = TreeNode(val = 3, left=None, right= None), right=None))

sol = Solution()
print(sol.isSameTree(tree,tree2))