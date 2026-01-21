# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        if not head:
            return False
        if not head.next:
            return True
        if not head.next.next and head.val!=head.next.val:
            return False
        # s = ''
        # while head:
        #     s+=str(head.val)
        #     head=head.next
        # for i in range(0,len(s)//2):
        #     if s[i]!=s[len(s)-i-1]:
        #         return False
        # return True
        if not head or not head.next:
            return True

        # Find midpoint
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Compare halves
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
