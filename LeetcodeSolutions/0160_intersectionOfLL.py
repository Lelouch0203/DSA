# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        d1= headA
        d2 = headB
        while d1!=d2:
            d1 = headB if not d1 else d1.next
            d2 = headA if not d2 else d2.next 
        return d1