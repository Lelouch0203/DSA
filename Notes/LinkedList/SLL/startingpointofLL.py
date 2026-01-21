class Node:
    def __init__(self,x):
        self.data = x
        self.next : 'Node|None' = None
        
def start(head):
    slow = head
    fast = head
    while slow and fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow==fast:
            slow = head
            while slow :
                if slow == fast:
                    return slow
                slow = slow.next
                fast = fast.next
        
    return None

head = Node(3)
head.next = Node(2)
head.next.next = Node(0)
head.next.next.next = Node(-4)

# Create cycle (last node points to node with value 2)
head.next.next.next.next = head.next

