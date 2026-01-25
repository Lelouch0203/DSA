class Node:
    def __init__(self,x):
        self.next:'Node|None' = None
        self.val = x
#from back , so use slow fast
def remove(head,n):
    if not head.next:
        return None
    slow = head
    fast = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next    
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head

head = Node(17)
head.next = Node(15)
head.next.next = Node(8)
head.next.next.next = Node(12)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next = Node(4)

h = remove(head,2)
while h:
    print(h.val,end=" ")
    h=h.next
