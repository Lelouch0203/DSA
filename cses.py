n = int(input())
def oe(n):
    if n == 1:
        print(1)
        
        return
    if n<4:
        print("NO SOLUTION")
        return
    x=n
    for i in range(n,0,-1):
        if i%2!=0:
            print(i,end=" ")
    for i in range(n,0,-1):
        if i%2==0:
            print(i,end=" ")
oe(n)
        