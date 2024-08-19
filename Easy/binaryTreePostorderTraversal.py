from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        temp = self.postorderTraversal(root.left)

        temp2 = self.postorderTraversal(root.right) 

        return temp+ temp2 + [root.val]
    
sol = Solution()

tree = TreeNode(val = 1, right=TreeNode(val = 6, left = TreeNode(2),right=TreeNode(3)))

print(sol.postorderTraversal(tree))