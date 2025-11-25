class Node:
    def __init__(self,x):
        self.val = x
        self.next = None
        
# def create_linked_list():
head = Node(1)
current = head
for i in range(2, 11):
    current.next = Node(i)
    current = current.next
key = [8,11]
count = 0
while head:
    count+=1
    if head.val == key[1]:
        print(f"found at {count}")
        break
    head=head.next
print(f"traversed {count} nodes and not found")