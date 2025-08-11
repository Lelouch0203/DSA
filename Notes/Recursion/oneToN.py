def funcc(i,n):
    if i>n:
        return
    else:
        print(i,end=" ")
        i+=1
        funcc(i,n)
funcc(1,15)