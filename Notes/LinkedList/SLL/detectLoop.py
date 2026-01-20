class Node:
    def __init__(self,x) :
        self.next : 'None | Node' = None
        self.data = x
        
head = Node(1)

head.next = Node(2) 
temp = head.next
head.next.next = Node(3)
head.next.next.next = temp



def loop(head):
 
    visited = set()
    temp = head
    while temp: 
        if temp in visited:
            return True
        visited.add(temp)
        temp = temp.next
    return False
print(loop(head))


def loopOP(head):
    slow = head
    fast = head
    while slow and fast and fast.next:
        if slow == fast:
            return True
        slow=slow.next
        fast = fast.next.next
        
    return False
