from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        pA, pB = headA, headB

        while pA != pB:
            pA = pA.next if pA else headB
            print('Pa: ', pA.val)

            pB = pB.next if pB else headA

            print('Pb: ', pB.val)

        return pB


sol= Solution()

