class Node:
    def __init__(self,val,next=None):
        self.val = val 
        self.next = next 
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = Node(0)
        curr = dummy
        carry = 0
        p, q = l1, l2
        while p or q or carry:
            x = p.val if p else 0
            y = q.val if q else 0
            s = x + y + carry
            carry = s // 10
            curr.next = Node(s % 10)
            curr = curr.next
            if p:
                p = p.next
            if q:
                q = q.next
        return dummy.next
l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)
l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

obj = Solution()
head = obj.addTwoNumbers(l1,l2)

# Print list after deletion
temp = head
while temp:
    print(temp.val, end=" ")
    temp = temp.next