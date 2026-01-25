class Node:
    def __init__(self,x):
        self.next:'Node|None' = None
        self.val = x
def middel(head):
    slow = head 
    fast = head
    if not head.next:
        return None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
        
    prev.next = slow.next
    return head
    
head = Node(17)
head.next = Node(15)
head.next.next = Node(8)
head.next.next.next = Node(12)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next = Node(4)

ans = middel(head)
while ans:
    print(ans.val,end=" ")
    ans=ans.next
