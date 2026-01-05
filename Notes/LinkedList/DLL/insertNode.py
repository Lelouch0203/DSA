class Node:
    def __init__(self,val,next_node = None, prev_node= None):
        self.data = val 
        self.next = next_node
        self.back = prev_node
    
def arrtoDLL(arr):
    head = Node(arr[0])
    prev = head 
    
    for i in range(1,len(arr)):
        temp = Node(arr[i],None,prev)
        prev.next=temp
        prev = temp 
        
    return head 
def printList(head):
    while head :
        print(head.data,end=" ")
        head= head.next
    print()
def insertAtTrail(head,node):
    newNode = Node(node)
    if not head:
        return newNode
    tail = head
    while tail.next:
        tail = tail.next 
        
    tail.next = newNode
    newNode.back = tail
    return head
if __name__ == "__main__":
    arr = [12, 5, 8, 7, 4]  # Initialize an array
    head = arrtoDLL(arr)  # Convert the array to a doubly linked list

    print("Doubly Linked List Initially:")
    printList(head)  # Print the doubly linked list

    print("\nDoubly Linked List After Inserting at the tail with value 10:")
    head = insertAtTrail(head, 10)  # Insert a node with value 10 at the end
    printList(head)  # Print the updated doubly linked list