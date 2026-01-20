class Node:
    def __init__(self,x): 
        self.data = x
        self.next : 'Node | None' = None
        
head = Node(1)
current = head
for i in range(2, 11):
    current.next = Node(i)
    current = current.next
    
def reverse(head):
    if not head or not head.next:
        return head
    newHead = reverse(head.next)
    front = head.next
    front.next = head
    head.next = None
    return newHead

ans = reverse(head)
while ans :
    print(ans.data)
    ans = ans.next
