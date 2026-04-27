# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=head
        slow=head
        None_found=True
        while  fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                None_found=False
                break
        if None_found:
            return None
        else :
            slow=head
            while slow!=fast:
                slow=slow.next
                fast=fast.next
        return slow
                
        
