class Node:
    def __init__(self,x):
        self.next:'Node|None' = None
        self.val = x
def intersect(h1,h2):
    d1= h1
    d2 = h2
    while d1!=d2:
        d1 = h2 if not d1.next else d1.next
        d2 = h1 if not d2.next else d2.next 
    return d1.val

head1 = Node(1)
head1.next=Node(2)
head1.next.next = Node(3)
head1.next.next.next=Node(4)


head2 = Node(5)
head2.next = Node(6)
head2.next.next = head1.next.next

print(intersect(head1,head2))