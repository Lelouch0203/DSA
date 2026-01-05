class Node:
    def __init__(self,val,next_node=None,prev_node=None):
        self.data = val 
        self.next = next_node
        self.back = prev_node
        
def arrtoDLl(arr):
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

def delNode(head,k):
    temp = head
    while temp.next:
        if temp.data == k:
            temp.data=temp.next.data
            temp.next=temp.next.next
            temp.next.prev = temp
            break
        temp = temp.next
    return head
if __name__ == "__main__":
    arr = [12, 5, 8, 7, 4]  # Initialize an array
    head = arrtoDLl(arr)  # Convert the array to a doubly linked list

    print("Doubly Linked List Initially:")
    printList(head)  # Print the doubly linked list
    head = delNode(head,5)
    printList(head)