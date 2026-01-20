class Node:
    def __init__(self,x):
        self.data = x
        self.next :'Node | None' = None
class Solution:
    def reverseLL(self, head):
        if not head.next:
            return head
        Next = None
        curr = head
        prev = None
        while curr:
            Next = curr.next
            curr.next = prev 
            prev = curr
            curr = Next
        return prev
    
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

obj = Solution()
head = obj.reverseLL(head)
while head:
    print(head.data)
    head = head.next
    
