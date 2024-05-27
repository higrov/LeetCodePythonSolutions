from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return str(self.val)
    

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []
        subtree = []

        while root or subtree: 
            
            while root:
                subtree.append(root)
                root = root.left
            
            root = subtree.pop()
            result.append(root.val)

            root = root.right
        
        return result
        

tree = TreeNode(val = 1, left = TreeNode(val= 4, left = TreeNode(val = 5, left=None, right= None), right=TreeNode(val = 6, left = None,right=None)), right= TreeNode(val= 2, left = TreeNode(val = 3, left=None, right= None), right=None))
sol = Solution()
print(sol.inorderTraversal(tree))