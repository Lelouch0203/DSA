class Node:
    def __init__(self,x):
        self.data = x
        self.next : 'Node|None' = None
        
def lenofloop(head):
    slow = head
    fast = head
    while slow and fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow==fast:
            
            pook = slow
            pook = pook.next
            cnt =1
            while pook!=slow:
                cnt +=1
                pook = pook.next

            return cnt                
            
        
    return None

head = Node(3)
head.next = Node(2)
head.next.next = Node(0)
head.next.next.next = Node(-4)
head.next.next.next.next = Node(5)

# Create cycle (last node points to node with value 2)
head.next.next.next.next.next = head.next

print(lenofloop(head))