class Node:
    def __init__(self,x):
        self.next:'Node|None' = None
        self.val = x
def mid(head):
    slow = head
    fast = head.next
    while fast and fast.next:
        slow=slow.next 
        fast = fast.next.next
    return slow

def merge(l1,l2):
    dummy = Node(-1)
    temp = dummy
    while l1 and l2:
        if l1.val<=l2.val:
            temp.next = l1
            l1=l1.next
        else:
            temp.next = l2
            l2 = l2.next
        temp = temp.next
            
    if l1:
        temp.next = l1
    else:
        temp.next = l2
    return dummy.next


def sort(head):
    if not head.next:
        return head
    middle = mid(head)
    right = middle.next
    middle.next = None
    left = head
    
    left = sort(left)
    right = sort(right)
    
    return merge(left,right)


head = Node(17)
head.next = Node(15)
head.next.next = Node(8)
head.next.next.next = Node(12)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next = Node(4)

ans = sort(head)
while ans:
    print(ans.val,end=" ")
    ans = ans.next  