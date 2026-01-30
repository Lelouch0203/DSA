def insert(stack,top):
    if not stack:
        stack.append(top)
        return 
    val = stack.pop()
    insert(stack,top)
    stack.append(val)

s=[1,2,3,4]
def rev(stack):
    if not stack:
        return 
    top= stack.pop()
    rev(stack)
    insert(stack,top)
    
rev(s)

print(s)