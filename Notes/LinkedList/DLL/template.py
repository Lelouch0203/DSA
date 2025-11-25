class Node:
    def __init__(self,val,next=None,prev=None):
        self.data = val 
        self.next = next
        self.prev = prev
        
arr = [2, 5, 8, 7]
head = Node(arr[0])
head.next = Node(arr[1])
head.next.prev = head
head.next.next = Node(arr[2])
head.next.next.prev = head.next
temp = head.next.next
print(temp.prev.prev.data)

 
 



