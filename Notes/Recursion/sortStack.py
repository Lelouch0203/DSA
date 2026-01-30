def insert(ele,stack):
    if not stack or ele<=stack[-1]:
        stack.append(ele)
        return 
    val = stack.pop()
    insert(ele,stack)
    stack.append(val)
    
def sort(stack):
    if stack:
        ele = stack.pop()
        sort(stack)
        insert(ele,stack)    
        
s = [4,1,3,2]
sort(s)
print(s)