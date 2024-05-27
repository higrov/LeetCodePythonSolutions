from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2: 
            return list1
        else:
            if list1.val <= list2.val: 
                temp = list1
                temp.next = self.mergeTwoLists(list1.next, list2)
            else:
                temp = list2
                temp.next = self.mergeTwoLists(list1, list2.next)
            

            return temp
        
list1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val = 4)))
list2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val = 4)))
sol = Solution()

print(sol.mergeTwoLists(list1,list2))