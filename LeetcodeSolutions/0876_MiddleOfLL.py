# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self,head):
        if not head.next:
            return head
        if not head.next.next:
            return head.next
        
        slow = head 
        fast = head 
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        return slow
            
