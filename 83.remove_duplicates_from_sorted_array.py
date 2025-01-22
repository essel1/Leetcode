from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_head = head
        
        while current_head and current_head.next:
            while current_head.next and current_head.next.val == current_head.val:
                current_head.next = current_head.next.next
            current_head = current_head.next                
        return head
                
                
            
    
if __name__ == "__main__":
    
    output = Solution().deleteDuplicates(head=[1,1,2])
    print(output)        