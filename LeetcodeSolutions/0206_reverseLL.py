# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if not head:
            return None
        if not head.next:
            return head
        prev = None 
        curr = head
        Next = None
        while curr:
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
        return prev