class Node:
    def __init__(self,val,next_node=None,prev_node=None):
        self.data = val 
        self.next = next_node
        self.prev = prev_node
def arrtoDLL(arr):
    head = Node(arr[0])
    prev = head
    for i in range(1,len(arr)):
        temp = Node(arr[i],None,prev)
        prev.next = temp
        prev = temp
        
    return head

def revDLL(head):
    temp = None
    curr = head
    while curr is not None:
        temp = curr.prev
        curr.prev = curr.next 
        curr.next = temp
        curr = curr.prev
    
    if temp is not None:
        head = temp.prev
        
    return head
