class Node:
    def __init__(self,x) :
        self.next : 'None | Node' = None
        self.data = x
        
head = Node(3)
head.next = Node(2)
head.next.next = Node(0)
head.next.next.next = Node(-4)

# Create cycle (last node points to node with value 2)
head.next.next.next.next = head.next



def loop(head):
 
    visited = set()
    temp = head
    while temp: 
        if temp in visited:
            print(temp.data)
            return True
        visited.add(temp)
        temp = temp.next
    return False
print(loop(head))


def loopOP(head):
    slow = head
    fast = head
    while slow and fast and fast.next:
        slow=slow.next
        fast = fast.next.next
        
        if slow == fast:
            print(slow.data)
            return True
    return False
print(loopOP(head))