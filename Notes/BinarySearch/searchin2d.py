def search2d(matrix,target):
    m=len(matrix)
    n=len(matrix[0])
    
    l=0
    r=m*n-1
    while l<=r:
        mid=(l+r)//2
        row = mid//n
        col = mid%n
        if matrix[row][col]==target:
            return True
        elif matrix[row][col]>target:
            r=mid-1
        else:
            l=mid+1
            
    return False

print(search2d([[1,2,3,4],[5,6,7,8],[8,9,10,11]],12))