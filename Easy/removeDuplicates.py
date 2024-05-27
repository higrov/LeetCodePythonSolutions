from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    def __repr__(self):
        return f"ListNode({self.val}, {self.next.__repr__()})"
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pt1 = head

        while pt1 is not None:
            pt2 = pt1.next
            while pt2 is not None and pt1.val == pt2.val:
                pt1.next = pt2.next
                pt2 = pt2.next
            
            pt1 = pt2

        return head
    
sol = Solution()
list1 = ListNode(val = 1, next= ListNode(val = 1, next= ListNode(val = 2, next= ListNode(val = 3, next = ListNode(val = 3, next = None)))))
print(sol.deleteDuplicates(list1))

