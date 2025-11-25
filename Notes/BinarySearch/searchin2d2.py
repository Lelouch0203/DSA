def search2d2(matrix,target):
    m=len(matrix)
    n=len(matrix[0])
    row=0
    col=n-1
    
    while row < m and col >= 0 :
        print(matrix[row][col])
        if matrix[row][col]==target:
            return True
        elif matrix[row][col]<target:
            row+=1
        else:
            col-=1
            
    return False

print(search2d2([[-5]],-5))
        