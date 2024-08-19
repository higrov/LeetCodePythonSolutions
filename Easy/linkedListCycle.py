from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        record = []

        if head is None: 
            return False
        
        while head.next: 
            if head in record: 
                return True 
            record.append(head)
            
            head = head.next
        
        return False