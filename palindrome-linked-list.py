# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        end = head
        middle = head

        # Find middle
        while end and end.next:
            end = end.next.next
            middle = middle.next

        # Skip middle if odd
        if end:
            middle = middle.next

        # Reverse second half
        current_node = middle
        prev = None

        while current_node:
            nxt = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = nxt

        # Compare
        check_node = head
        second = prev

        while second:
            if check_node.val != second.val:
                return False
            check_node = check_node.next
            second = second.next

        return True
