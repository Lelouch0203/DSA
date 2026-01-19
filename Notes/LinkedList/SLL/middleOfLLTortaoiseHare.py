class Node:
    def __init__(self, x):
        self.data = x
        self.next: 'Node | None' = None
        
    
    
class Solution:
    def middleNode(self,head):
        if not head.next:
            return head 
        if not head.next.next:
            return head.next
        
   
        #my approach or brute force
        
        # cnt = 0
        # temp = head
        # while temp.next:
        #     cnt+=1
        #     temp = temp.next
        # if cnt %2!=0:
        #     cnt+=1
        # cnt//=2
        # for _ in range(cnt):
        #     head = head.next
        # return head 
    
    
        #tortoise Hare 
        slow = head
        fast = head 
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

            
        
head = Node(1)
head.next = Node(2) 
head.next.next = Node(3)
obj = Solution()
head = obj.middleNode(head)
print(head.data)
    
