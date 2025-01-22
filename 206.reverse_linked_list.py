from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_head = head
        current_prev = None
        while current_head:
            
            current_next = current_head.next
            current_head.next = current_prev

            current_prev = current_head
            current_head = current_next
            
        
        return current_prev   
    
    
        # if head.next.next == None:
        #     head.next.next = head
        #     head.next = None
        #     return head

        # reverse(head.next)