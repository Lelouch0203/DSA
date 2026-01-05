class Node:
    def __init__(self,x):
        self.val = x
        self.next = None
head = Node(1)
current = head
for i in range(2, 11):
    current.next = Node(i)
    current = current.next
def printList(head):
    while head :
        print(head.val,end=" ")
        head= head.next
    print()
def middle(head):
    if not head.next:
        return head
    if not head.next.next:
        return head.next
    cnt = 0
    temp = head
    while temp.next:
        cnt+=1
        temp = temp.next
    if cnt %2!=0:
        cnt+=1
    cnt//=2
    for _ in range(cnt):
        head = head.next
    return head 
printList(head)
printList(middle(head))