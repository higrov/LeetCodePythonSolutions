from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSameTree( p: Optional[TreeNode], q: Optional[TreeNode]):
            if p is None and q is None: 
                return True

            elif p is None and q is not None or q is None and p is not None: 
                return False
            else: 
                return (p.val == q.val ) and isSameTree(p.left,q.right) and isSameTree(p.right, q.left)

        return isSameTree(root.left,root.right)


tree = TreeNode(val = 1, left = None , right= TreeNode(val= 2, left = TreeNode(val = 3, left=None, right= None), right=None))

tree2 = TreeNode(val = 1, left = TreeNode(val= 2, left = TreeNode(val = 3, left=None, right= None), right=None) , right= TreeNode(val= 2, left = TreeNode(val = 3, left=None, right= None), right=None))

sol = Solution()

print(sol.isSymmetric(tree2))