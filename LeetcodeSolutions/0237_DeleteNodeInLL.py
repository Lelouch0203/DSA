class Node:
    def __init__(self,val):
        self.next: 'Node | None' = None
        self.data = val
    
class Solution:
    def deleteNode(self, node):
        node.data = node.next.data
        node.next = node.next.next
        return head
        

head = Node(1)
head.next = Node(2) 
head.next.next = Node(3)
obj = Solution()
head = obj.deleteNode(head.next)


temp = head
while temp:
    print(temp.data, end=" ")
    temp = temp.next