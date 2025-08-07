def secLarge(arr):
    # arr=sorted(arr)
    # return arr[-2]
    
     
    large=float('-inf')
    secondlrge=float('-inf')
    
    for i in arr:
        if i > large:
            secondlrge=large
            large=i
#another approach is to find the large first and then check for the secoond large using if condition
        if i > secondlrge and i != large:
            secondlrge=i
    return secondlrge
print(secLarge([2,5,1,3,0]))