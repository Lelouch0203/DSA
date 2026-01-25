class Node:
    def __init__(self,x):
        self.next:'Node|None' = None
        self.val = x
        
def oddeve(head):
    evehead = evetail = None
    oddhead = oddtail = None
    curr = head
    while curr:
        if curr.val%2==0:
            if not evehead:
                evehead = evetail = curr
                
            else:
                evetail.next = curr
                evetail = curr
                
        else:
            if not oddhead:
                oddhead = oddtail = curr
            else:
                oddtail.next = curr
                oddtail = curr
        curr = curr.next
        
    if not evehead:
        return oddhead
    if not oddhead:
        return evehead
    
    evetail.next = oddhead
    oddtail.next = None
    return evehead

head = Node(17)
head.next = Node(15)
head.next.next = Node(8)
head.next.next.next = Node(12)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next = Node(4)

ans = oddeve(head)
while ans:
    print(ans.val)
    ans=ans.next