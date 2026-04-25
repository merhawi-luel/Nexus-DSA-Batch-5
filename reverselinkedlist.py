# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_node=head
        prev=None
        while new_node :
            nxt=new_node.next
            new_node.next=prev
            prev=new_node
            new_node=nxt

        
        return prev


        
