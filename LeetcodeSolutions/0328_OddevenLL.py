# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        oh = ot = None
        eh = et = None
        curr = head
        while curr:
            if curr.val % 2 == 0:
                if not eh:
                    eh = curr
                    et = curr
                else:
                    et.next = curr
                    et = curr

            else:
                if not oh:
                    oh = curr
                    ot = curr
                else:
                    ot.next = curr
                    ot = curr

            curr = curr.next

        if not oh:
            return eh
        if not eh:
            return oh

        et.next = oh
        ot.next = None
        return eh